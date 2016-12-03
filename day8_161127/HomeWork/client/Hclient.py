import socket
import os
import sys
import time

client = socket.socket()
client.connect(("127.0.0.1", 8001))
sys.path.append(os.getcwd())

# print(sys.path, os.getcwd())
print("""
welcome:
    执行命令直接输入即可.
    下载文件 get a.txt
    上传文件 put a.txt
    输入 q 退出程序
""")
while True:
    msg = str(input("请输入[q]:").strip())
    if len(msg) == 0: continue
    elif msg == "q":
        break
    elif msg.startswith("put"):
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
            time.sleep(1)
            print(file)
            with open(file, "rb") as read_file:
                for line in read_file:
                    print("send data ......", line)
                    client.send(line)
        else:
            print("%s 此文件不存在" % msg_li[1])
        continue
    elif msg.startswith("get"):
        msg_data = msg.encode()
        msg_li = msg.split(" ")
        client.send(msg_data)
        check = int(client.recv(1024).decode())
        if check:
            # data_size = client.recv(1024) #获取文件大小
            base_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
            print(base_list)
            if msg_li[1] in base_list:
                file_name = "%s/%s_new" % (os.path.dirname(os.path.abspath(__file__)), msg_li[1])
            else:
                file_name = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), msg_li[1])
            print(file_name)
            with open(file_name, "wb") as write_file:
                receive = client.recv(1024)
                print("receive size : ", receive)
                receive_size = int(receive.decode())
                source_size = 0
                new_data = b''
                print("开始接收数据,文件大小:", receive_size)
                while source_size < receive_size:
                    new_data = client.recv(1024)
                    print("接收数据: ", new_data.decode())
                    source_size += len(new_data)
                    print(source_size, receive_size)
                    write_file.write(new_data)
            print("接收完成.....")
        else:
            print("文件不存在", msg_li[1])
            continue
    else:
        client.send(msg.encode())
        # print("send", msg)
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
        print("接收到服务器的信息:\n", received_data.decode())
        # print("接收到服务器的信息:\n", received_data.decode(), data_len)
    # print("接收到服务器的信息:", data)
    # dataa = client.recv(1024)
client.close()
