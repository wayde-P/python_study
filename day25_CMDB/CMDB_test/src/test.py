from config import settings
class BasePlugin(object):
    """
    约束.公共方法
    """

    def agent_cmd(self,cmd):
        pass
        # import subprocess
    def ssh_cmd(self,cmd):
        pass
    def salt_cmd(self,cmd):
        pass

    def cmd(self,cmd):
        if settings.MODE = "agent":
            result = self.agent_cmd(cmd)
        elif  settings.MODE = "ssh":
            result = self.ssh_cmd(cmd)
        elif  settings.MODE = "salt":
            result = self.salt_cmd(cmd)
        else:
            raise Exception("配置文件MODE设置错误")

    def execute(self):
        return self.linux()

    def linux(self):
        raise NotImplementedError("插件必须实现linux方法")

class DiskPlugin(BasePlugin):
