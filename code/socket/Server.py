# 文件名：Server.py
import socket

server = socket.socket()
host = socket.gethostname()
port = 15656
server.bind((host, port))
server.listen(5)
while True:
    c, addr = server.accept()
    print("连接地址：", addr)
    server.send('123'.encode())
    server.close()
