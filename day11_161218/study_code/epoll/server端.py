import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)
server.setblocking(0)  # 设置不阻塞

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
                data = s.recv(1024)  # 接收数据
                print("recv data from [%s]:[%s]" % (s.getpeername(), data.decode()))
                msg_queue[s].put(data)  # 往自己专用的队列里面添加处理完成的数据
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
