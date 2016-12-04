import socket
import os
import json

client = socket.socket()
client.connect(("localhost", 9000))

while True:
    choice = input(">>>").strip()
    if len(choice) == 0: continue
    cmd_list = choice.split()
    if cmd_list[0] == "put":
        if len(cmd_list) == 1:
            print("没有文件名")
            continue
        filename = cmd_list[1]
        if os.path.isfile(filename):
            base_filename = filename.split("/")
            data_header = {
                "action": "put",
                "filename": base_filename,
                "size": os.path.getsize(filename)
            }
            client.send(json.dumps(data_header).encode())
            file_obj = open(filename, "rb")
            for line in file_obj:
                client.send(line)
        else:
            print("不是正常的文件")
            continue


    elif cmd_list[0] == "get":
        pass
