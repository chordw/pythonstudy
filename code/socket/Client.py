# 文件名：Client.py
import socket
client = socket.socket()
host = socket.gethostname()
port = 15656
client.connect((host, port))
while True:
    print(client.recv(1024))
    client.close()
