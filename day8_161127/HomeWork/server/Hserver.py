#!/bin/env python3
import socket
import subprocess
import os
import time

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
            receive_data = data.decode()  # 获取传入的文件信息
            base_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
            # print("base_list:", base_list)
            if receive_data.startswith("put"):
                msg = receive_data.split(" ")
                if msg[1] in base_list:
                    file_name = "%s/%s_new" % (os.path.dirname(os.path.abspath(__file__)), msg[1])
                else:
                    file_name = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), msg[1])
                print("file name is:", file_name)
                with open(file_name, "wb") as write_file:
                    receive_size = int(conn.recv(1024).decode())
                    source_size = 0
                    new_data = b''
                    print("开始接收数据,文件大小:", receive_size)
                    while source_size < receive_size:
                        # source_size = os.path.getsize(file_name)
                        print("接收数据.....")
                        new_data = conn.recv(1024)
                        print(new_data)
                        source_size += len(new_data)
                        print(source_size, receive_size)
                        write_file.write(new_data)
                print("接收完成.....")
                continue
            elif receive_data.startswith("get"):
                msg = receive_data.split(" ")  # 获取传入的文件信息
                base_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
                if msg[1] in base_list:
                    file = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), msg[1])
                    conn.send(b'1')
                    print("get file name is :", file)
                    # file_msg = {"file_name": msg_li[1],
                    #             "file_size": os.path.getsize(file)}
                    # send_data = eval(file_msg)
                    conn.send(str(os.path.getsize(file)).encode())
                    time.sleep(1)
                    print(file)
                    with open(file, "rb") as read_file:
                        for line in read_file:
                            # print("send data: ", line.decode())
                            conn.send(line)
                else:
                    conn.send(b'0')
            else:
                res_obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                res = res_obj.stdout.read()
                data_len = str(len(res)).encode()
                time.sleep(0.2)
                conn.send(data_len)
                print(data_len)
                conn.send(res)
        except ConnectionResetError as e:
            break
        except BrokenPipeError as e:
            break

server.close()
