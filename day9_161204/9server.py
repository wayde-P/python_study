import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9000))
s.listen(5)

while True:
    conn, client_addr = s.accept()
    while True:
        data = conn.recv(1024)
        print("received data:", data)
        data = json.loads(data.decode())

        if data.get('action') is not None:
            if data['action'] == "put":
                file_obj = open(data['filename'], "wb")
                received_size = 0
                while received_size < data["size"]:
                    recv_data = conn.recv(1024)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                else:
                    print("successfully receive")
                    file_obj.close()
