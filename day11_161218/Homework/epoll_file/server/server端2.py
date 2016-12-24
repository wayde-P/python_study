import select
import socket
import queue
import time, os, subprocess

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)
server.setblocking(1)

inputs = [server]  # 需要监听server自己
outputs = []  # 创建空列表,用来保存有消息的连接
msg_queue = {}  # 创建消息队列的字典

while True:
    r_list, w_list, exception_list = select.select(inputs, outputs, inputs)
    for s in r_list:  # 如果r_list里面有新连接了
        if s is server:  # 如果新的连接是个socket,说明是个新连接进来了
            conn, addr = s.accept()  # 建立连接
            print("got a new conn ", conn, addr)
            inputs.append(conn)  # 让select也去监听这个新连接
            msg_queue[conn] = queue.Queue()  # 为新连接创建消息队列用来存储执行结果
        else:  # 说明进来的不是一个新连接,而是已经创建的连接有接收到数据
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
                            new_data = s.recv(1024)
                            print(new_data)
                            source_size += len(new_data)
                            print(source_size, receive_size)
                            write_file.write(new_data)
                        conn.send(b'1')
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
                if s not in outputs:
                    outputs.append(s)  # 等下次select的时候,确保w_list的数据能返回给客户端
            except ConnectionResetError as e:
                print("conn closed", s.getpeername(), e)
                # 当连接出问题了,以下为清空这个socket对象
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                del msg_queue[s]
    for s in w_list:
        # 给客户端返回准备好的数据
        try:
            data = msg_queue[s].get_nowait()
            s.send(data.upper())
        except queue.Empty as e:
            outputs.remove(s)
