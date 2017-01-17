import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
    f = open('s5.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    import time
    data = data.replace('@@@@@@', str(time.time()))
    client.send(bytes(data, encoding='utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8003))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
