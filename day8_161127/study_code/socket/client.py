import socket

client = socket.socket()
client.connect(("192.168.0.34", 8001))
while True:
    msg = input("请输入:").strip()
    if len(msg) == 0: continue
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
