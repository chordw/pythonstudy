import logging

logging.basicConfig(level=logging.INFO)

import asyncio

from aiohttp import web


def index(request):
    logging.info("请求%s" % request)
    text = '<h3>Hello</h3>'
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/www/static/index.html',index)

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    logging.info('server started at http://127.0.0.1:8000...')
    return srv


import aiomysql


# <editor-fold desc="创建数据库连接池">
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info("create database connect poll...")
    global _pool
    _pool = yield from aiomysql.create_pool(host=kw.get('host', 'localhost')
                                            , port=kw.get('port', 3306)
                                            , user=kw['user']
                                            , password=kw['password']
                                            , db=kw['db']
                                            , charset=kw.get('charset', 'utf-8')
                                            , autocommit=kw.get('autocommit', True)
                                            , maxsize=kw.get('maxsize', 10)
                                            , minsize=kw.get('minsize', 1)
                                            , loop=loop)


# </editor-fold>

# <editor-fold desc="查询语句">
@asyncio.coroutine
def select(sql, args, size=None):
    logging.info(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


# </editor-fold>

# <editor-fold desc="插入、删除、更新语句">
@asyncio.coroutine
def execute(sql, args):
    logging.info(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected


# </editor-fold>

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
