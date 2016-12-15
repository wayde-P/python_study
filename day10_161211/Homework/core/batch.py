import optparse
import configparser
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings


def main():
    paser = optparse.OptionParser()
    paser.add_option("-s", "--host", dest="host", help="server ipv4 address")
    paser.add_option("-g", "--group", dest="group", help="server groups")
    paser.add_option("-c", "--command", dest="command", help="command")
    options, args = paser.parse_args()
    # print(options)
    if (options.host is not None or options.group is not None) and options.command is None:
        exit("请带上 -c \"你的命令\"")
    elif options.host is None and options.group is None:
        exit("请输入 -h 或 -g ")
    # elif (options.host is not None) or (options.group is not None):
    else:
        server_list = fetch_server_list(options.host, options.group)
        print(server_list)


def fetch_server_list(hosts, groups):
    config = configparser.ConfigParser()
    config.read(settings.host_file)  # 读取host配置文件
    config.read(settings.group_file)  # 读取group配置文件
    all_server = config.sections()
    # print(all_server)
    server_list = []  # 用来存储服务器列表

    if hosts is not None:  # 传入的host不为空
        host_list = hosts.split(",")  # 切割传入的host
        for host in host_list:
            if host in all_server:  # host存在配置文件里
                server_list.append(host)  # host加入列表里
    if groups is not None:
        group_list = groups.split(",")
        for group in group_list:
            if group in all_server:
                for host in config[group]["ip"].split(","):
                    server_list.append(host)
            else:
                print("%s not in group.cfg" % group)

    return set(server_list)


if __name__ == "__main__":
    main()
