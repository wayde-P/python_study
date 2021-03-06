import socketserver
import configparser
import os, sys
import hashlib
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'lock_test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename doesn't provided",
    256: "File doesn't exist on server",
    257: "ready to send file",
    258: "md5 verification",
    259: "Invalid dir",
    260: "dir not in home_dir",
    261: "change to new dir",
    262: "send dir and file list"
}


class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            if not self.data:
                print("client closed...")
                break
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                print("---->", hasattr(self, "_auth"))
                if hasattr(self, "_%s" % data.get('action')):
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data=None):
        """向客户端返回数据"""
        response = {'status_code': status_code, 'status_msg': STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)

        user = self.authenticate(data.get("username"), data.get("password"))  # 调用验证模块
        if user is None:  # 返回为空则发送错误
            self.send_response(253)
        else:  # 否则通过验证,然后定义初始环境变量
            print("passed authentication", user)
            self.user = user
            # 发送验证通过
            self.send_response(254)
            # 定义家目录
            self.user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
            # 定义当前目录
            self.current_dir = self.user_home_dir

    def authenticate(self, username, password):
        """验证用户合法性，合法就返回用户数据"""
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth..", username)
                config[username]["Username"] = username
                return config[username]

    def _put(self, *args, **kwargs):
        """client send file to server"""
        data = args[0]  # put file_name
        if data.get('filename') is None:  # 判断文件名是否存在
            self.send_response(255)
        self.user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])

        pass

    def _get(self, *args, **kwargs):
        data = args[0]  # get file_name
        if data.get('filename') is None:
            self.send_response(255)
        # user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
        file_abs_path = "%s/%s" % (self.user_home_dir, data.get('filename'))
        print("file abs path", file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size': file_size})
            self.request.recv(1)  # 等待客户端确认

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258, {'md5': md5_val})
                    print("send file done....")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done....")
        else:
            self.send_response(256)

    def _ls(self, *args, **kwargs):
        data = args[0]
        old_dir = self.current_dir
        if data is None:
            root, dirs, files = next(os.walk(self.current_dir))
        else:
            dir_name = {"dir": data}
            change_to_dir = self._cd(dir_name)
            root, dirs, files = next(os.walk(change_to_dir))

        send_list = {
            "dir_list": dirs,
            "file_list": files
        }
        self.current_dir = old_dir

    # 已经完成,待优化
    def _cd(self, *args, **kwargs):
        data = args[0]
        # if self.current_dir is None:
        #     old_current_dir = self.user_home_dir
        # else:
        #     old_current_dir = self.current_dir
        if data.get('dir') is None:
            self.current_dir = self.user_home_dir
        # elif data.get('dir') == '-':
        #     self.current_dir = old_current_dir
        else:
            new_dir = "%s/%s" % (self.current_dir, data.get('dir'))
            new_real_path = os.path.realpath(new_dir)
            if os.path.isdir(new_real_path):
                if self.user_home_dir in new_real_path:
                    self.current_dir = new_real_path
                    send_current_dir = {"dir": new_real_path}
                    self.send_response(261, send_current_dir)
                else:
                    self.send_response(260)
            else:
                self.send_response(259)
        return new_real_path

    def _pwd(self, *args):
        pass


if __name__ == "__main__":
    # HOST, PORT = "localhost", 9000
    print("welcom to wayde FTP")
