import socket
import os

client = socket.socket()
client.connect(("192.168.0.34", 8001))
while True:
    msg = str(input("请输入:").strip())
    if len(msg) == 0: continue
    if msg.startswith("put"):
        msg_li = msg.split(" ")
        # 判断文件是否存在
        if os.path.exists(msg_li[1]):
            file_msg = {"file_name": msg_li[1],
                        "file_size": os.path.getsize(msg_li[1])}
            client.send(file_msg)
            file = file_msg[1]
            with open(file) as read_file:
                for line in read_file:
                    client.send(line.encode())


        else:
            print("%s此文件不存在" % msg_li[1])

    client.send(msg.encode())
    print("send", msg)

    data_len = int(client.recv(1024).decode())  # 获取返回长度

    received_size = 0
    received_data = b''
    while received_size < data_len:
        data = client.recv(1024)  # 返回的数据
        received_data += data
        received_size += len(data)

    print("接收到服务器的信息:\n", received_data.decode(), data_len)
    # print("接收到服务器的信息:", data)
    # dataa = client.recv(1024)
