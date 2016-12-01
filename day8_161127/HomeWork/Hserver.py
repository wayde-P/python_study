#!/bin/env python3
import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8001))
server.listen(5)

while True:

    print("start".center(20, "-"))
    conn, client_addr = server.accept()
    print(conn, client_addr)
    while True:
        try:
            data = conn.recv(1024)
            print("recv from cli:", data)
            res_obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            res = res_obj.stdout.read()
            data_len = str(len(res)).encode()
            print(data_len)
            conn.send(data_len)
            conn.send(res)
        except ConnectionResetError as e:
            break

server.close()
