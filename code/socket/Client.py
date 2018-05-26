# 文件名：Client.py
import socket
try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("www.sina.com.cn",80))
    client.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buf = []
    while True:
        b= client.recv(1024)
        if b:
            buf.append(b)
        else:
            break
    data = b''.join(buf)
    print(data)
except IOError as e:
    print(e.args)
    exit(1)
