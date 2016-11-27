import socket
client = socket.socket()
client.connect(("127.0.0.1",8000))
while True:
    msg = input("请输入:").strip()
    if len(msg) == 0 : continue
    client.send(msg.encode())
    print("send",msg)
    data = client.recv(1024)
    print("接收到服务器的信息:",data)