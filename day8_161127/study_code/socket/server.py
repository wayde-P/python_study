import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000))
server.listen(5)
print("start".center(20,"-"))
conn,client_addr =  server.accept()
print(conn,client_addr)

while True:
    data = conn.recv(1024)
    print("recv from cli:",data)
    conn.send(b"got you messge")