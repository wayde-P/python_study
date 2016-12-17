import optparse
import configparser
import os
import sys
import multiprocessing as MP
import paramiko

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings


def main():
    paser = optparse.OptionParser()
    paser.add_option("-s", "--host", dest="host", help="server ipv4 address like : 192.168.1.1")
    paser.add_option("-g", "--group", dest="group", help="server groups like : webserver ")
    paser.add_option("-c", "--command", dest="command", help="to server exec command")
    options, args = paser.parse_args()
    # print(options)
    if (options.host is not None or options.group is not None) and options.command is None:
        exit("请添加选项 -c \"你的命令\"")
    elif options.host is None and options.group is None:
        exit("请添加选项 -h 或 -g ")
    else:
        server_list = fetch_server_list(options.host, options.group)
    run(server_list, options.command)


def launch(host, port, user, password, command):
    """ssh 远程执行命令函数"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    print("host: %s , command: %s,".center(40, "=") % (host, command))
    print(result.decode())
    print(str("end").center(40, "="))
    print("\n")
    ssh.close()


def run(server, command):
    """多进程并发模块"""
    p_list = []
    for host in server.keys():
        port = server[host]["port"]
        user = server[host]["user"]
        password = server[host]["password"]
        exec_command = command
        process = MP.Process(target=launch, args=(host, port, user, password, exec_command))
        process.start()
        p_list.append(process)

    for t in p_list:
        t.join()


def fetch_server_list(hosts, groups):
    """解析ip模块,对输入的ip和组进行组合,并去重.返回的是ip为key的字典"""
    config = configparser.ConfigParser()
    config.read(settings.host_file)  # 读取host配置文件
    config.read(settings.group_file)  # 读取group配置文件
    all_server = config.sections()
    # print(all_server)
    server_list = {}  # 用来存储服务器列表
    if hosts is not None:  # 传入的host不为空
        host_list = hosts.split(",")  # 切割传入的host
        for host in host_list:
            if host in all_server:  # host是否存在配置文件里
                server_list[host] = {}  # host加入字典里
                server_list[host]["user"] = config[host]["user"]
                server_list[host]["password"] = config[host]["password"]
                server_list[host]["port"] = int(config[host]["port"])
            else:
                print(host, "is not in host configure ")
    if groups is not None:
        group_list = groups.split(",")
        for group in group_list:
            if group in all_server:
                for host in config[group]["ip"].split(","):
                    if host in all_server:  # host是否存在配置文件里
                        server_list[host] = {}  # host加入字典里
                        server_list[host]["user"] = config[host]["user"]
                        server_list[host]["password"] = config[host]["password"]
                        server_list[host]["port"] = int(config[host]["port"])
                    else:
                        print(host, "is not in host configure ")
            else:
                print("%s not in group.cfg" % group)
    return server_list


if __name__ == "__main__":
    main()
