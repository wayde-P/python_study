import paramiko
import sys
import os
import socket
import select
import getpass
from paramiko.py3compat import u

tran = paramiko.Transport(('192.168.12.63', 22,))
tran.start_client()
tran.auth_password('alex', '123')

# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()

while True:
    # 监视用户输入和服务器返回数据
    # sys.stdin 处理用户输入
    # chan 是之前创建的通道，用于接收服务器返回信息
    # [chan,]
    # [sys.stdin,]
    readable, writeable, error = select.select([chan, sys.stdin, ], [], [], 1)
    # 服务端返回数据
    if chan in readable:
        try:
            x = u(chan.recv(1024))
            if len(x) == 0:
                print('\r\n*** EOF\r\n')
                break
            sys.stdout.write(x)
            sys.stdout.flush()
        except socket.timeout:
            pass
    # 在终端输入内容
    if sys.stdin in readable:
        # 读取一整行的数据
        inp = sys.stdin.readline()
        chan.sendall(inp)
chan.close()
tran.close()
