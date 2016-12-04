import socket

client = socket.socket()
client.connect(("localhost", 9001))
while True:
    data = input(">>>").strip()
    client.send(data.encode())
    recv_data = client.recv(1024)
    print(recv_data.decode())
