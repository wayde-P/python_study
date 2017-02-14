import paramiko


class SSH:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd

        self.transport = None

    def connect(self):
        self.transport = paramiko.Transport((self.host, self.port,))
        self.transport.connect(username=self.user, password=self.pwd)

    def cmd(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.read()

    def download(self, server_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        # 将location.py 上传至服务器 /s1-login/test.py
        # sftp.put('/s1-login/location.py', '/s1-login/test.py')
        # 将remove_path 下载到本地 local_path
        sftp.get(server_path, local_path)

    def upload(self, server_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        # 将location.py 上传至服务器 /s1-login/test.py
        # sftp.put('/s1-login/location.py', '/s1-login/test.py')
        # 将remove_path 下载到本地 local_path
        sftp.put(local_path, server_path)

    def close(self):
        self.transport.close()


obj = SSH('192.168.12.63', 22, 'alex', '123')
obj.connect()
# v = obj.cmd('ls')
v = obj.cmd('df')
print(v)
obj.close()
