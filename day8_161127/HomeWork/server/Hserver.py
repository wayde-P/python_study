#!/bin/env python3
import socket
import subprocess
import os

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
            receive_data = data.decode()
            base_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
            print("base_list:", base_list)
            if receive_data.startswith("put"):
                msg = receive_data.split(" ")
                if msg[1] in base_list:
                    file_name = "%s_new" % msg[1]
                else:
                    file_name = msg[1]
                print("file name is:", file_name)
                with open(file_name, "w+") as write_file:
                    receive_size = int(conn.recv(1024).decode())
                    source_size = 0
                    new_data = b''
                    print("开始接收数据,文件大小:", receive_size)
                    while source_size < receive_size:
                        print("接收数据.....")
                        new_data = conn.recv(1024).decode()
                        print(new_data)
                        source_size += len(new_data)
                        print(source_size, receive_size)
                        write_file.write(new_data)
                continue







            res_obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            res = res_obj.stdout.read()
            data_len = str(len(res)).encode()
            conn.send(data_len)
            print(data_len)
            conn.send(res)
        except ConnectionResetError as e:
            break
        except BrokenPipeError as e:
            break

server.close()
