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
    print(options)
    if options.command is None:
        exit("请带上-c \"你的命令\"")
    elif (options.host is not None) or (options.group is not None):
        server_list = fetch_server_list(options.host, options.group)


def fetch_server_list(hosts, group):
    config = configparser.ConfigParser()
    config.read(settings.host_file)
    config.read(settings.group_file)
    all_server = config.sections()
    print(all_server)
    server_list = []

    if hosts is not None:
        for host in hosts:
            if host in all_server:
                server_list.append(host)
    if group is not None:
        # for host in
        pass

        # print(config.sections())


if __name__ == "__main__":
    main()
