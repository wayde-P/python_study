import optparse
import configparser
import os
import sys
import paramiko
import multiprocessing as mp



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings


# config = configparser.ConfigParser()
# config.read(settings.host_file)
# config.read(settings.group_file)
# all_server = config.sections()
# print(config['192.168.1.1']['user'])
# for i in config['webserver']:
#     print(i)
#
# print(all_server)


def launch(host, port, user, password, command):
    # ssh_link=paramiko.Transport((host,port))
    # ssh_link.connect(username=user,password=password)
    # ssh = paramiko.SSHClient()
    # ssh._ssh_link = ssh_link
    # stdin,stdout,stderr = ssh.exec_command(command)
    # print(stdout.read())
    # ssh_link.close()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    print(result.decode())
    ssh.close()


t_list = []
# for i in range(5):
p = mp.Process(target=launch, args=(("192.168.0.101", 22, "root", "dianrudianru", "date")))
p.start()
# t_list.append(p)
#
# for t in t_list:
#     t.join()

# launch("192.168.0.101",22,"root","dianrudianru","df")
