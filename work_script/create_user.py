import pymysql
class Mysql(object):
    def __init__(self,host,port,user,password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def ex_conn(self):
        pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        return

    def ex_commnad(self,command):
        pass
