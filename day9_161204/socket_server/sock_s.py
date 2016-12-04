import socketserver


class MytTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            print("{} wrote:".format(self.client_address))
            print(self.data)

        self.request.send(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = 'localhost', 9001
    server = socketserver.ThreadingTCPServer((HOST, PORT), MytTCPHandler)
    server.serve_forever()
