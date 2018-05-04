# 文件名：Client.py
import socket
try:
    client = socket.socket()
    host = socket.gethostname()
    port = 15656
    client.connect((host, port))
    while True:
        print(client.recv(1024))
        client.close()
except IOError as e:
    print(e.args)
    exit(1)
