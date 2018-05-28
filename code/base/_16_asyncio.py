# <editor-fold desc="协程">


def consumer():
    r = ''
    while True:
        x = yield r
        if not x:
            break
        print("消费了：", x)
        r = '200,OK'
    r = '结束了'
    return r


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1;
        print("生产:", n)
        r = c.send(n)
        print("消费返回：", r)
    return "结束"


c = consumer()

c.send(None)
try:
    print("返回值：", c.send(1))
    print("返回值：", c.send(2))
    print("返回值：", c.send(3))
    print("返回值：", c.send(4))
    c.send(None)
except StopIteration as  e:
    print(e.value)

# </editor-fold>


# <editor-fold desc="asyncio">

import asyncio
import threading


@asyncio.coroutine
def hello():
    print("hello world")
    print(threading.current_thread())
    yield from asyncio.sleep(1)
    print("hello again")
    print(threading.current_thread())


@asyncio.coroutine
def world():
    print("hello world2")
    print(threading.current_thread())
    yield from asyncio.sleep(1)
    print("hello again2")
    print(threading.current_thread())


loop = asyncio.get_event_loop()

task = [hello(), world()]

loop.run_until_complete(asyncio.wait(task))


# loop.close()


# </editor-fold>

# <editor-fold desc="async await">

# async 替代 @asyncio.coroutine
# await 替代 yield from

async def hello():
    print("Hello world")
    r = await asyncio.sleep(1)
    print("hello again")


loop2 = asyncio.get_event_loop()
loop2.run_until_complete(hello())
loop2.close()
# </editor-fold>
