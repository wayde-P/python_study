import socket
import os
import sys

client = socket.socket()
client.connect(("127.0.0.1", 8001))
sys.path.append(os.getcwd())

print(sys.path, os.getcwd())
while True:
    msg = str(input("请输入:").strip())
    if len(msg) == 0: continue
    if msg.startswith("put"):
        msg_data = msg.encode()
        client.send(msg_data)
        base_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
        print(base_list)
        print(os.path.dirname(os.path.abspath(msg)))
        msg_li = msg.split(" ")
        # 判断文件是否存在
        if msg_li[1] in base_list:
            file = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), msg_li[1])
            print("file name is :", file)
            # file_msg = {"file_name": msg_li[1],
            #             "file_size": os.path.getsize(file)}
            # send_data = eval(file_msg)
            client.send(str(os.path.getsize(file)).encode())
            print(file)
            with open(file, "rb") as read_file:
                for line in read_file:
                    print("send data ......", line)
                    client.send(line)


        else:
            print("%s此文件不存在" % msg_li[1])
        continue

    client.send(msg.encode())
    print("send", msg)
    lenth = client.recv(1024)
    if len(lenth) > 0:
        data_len = int(lenth.decode())  # 获取返回长度
    else:
        continue

    received_size = 0
    received_data = b''
    while received_size < data_len:
        data = client.recv(1024)  # 返回的数据
        received_data += data
        received_size += len(data)

    print("接收到服务器的信息:\n", received_data.decode(), data_len)
    # print("接收到服务器的信息:", data)
    # dataa = client.recv(1024)
