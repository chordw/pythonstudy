def applicate(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,World!</h1>']

from wsgiref.simple_server import make_server

httd = make_server('',8000,applicate)
print('serving http on port 8000')

httd.serve_forever()