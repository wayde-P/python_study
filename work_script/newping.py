import paramiko
import time
import IPy
import os
import sys
import config
import re
import threading
import subprocess
import queue
import pymysql
import requests

basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(basedir)

net_segment = config.config
db_config = config.dbconfig
exclude_ip = config.exclude_ip
q = queue.Queue()


class SSH(object):
    def __init__(self, host, port, user, ):
        self.host = host
        self.port = port
        self.user = user
        self.private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        self.transport = None

    def connect(self):
        self.transport = paramiko.Transport((self.host, self.port,))
        self.transport.connect(username=self.user, pkey=self.private_key)

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read()

    def close(self):
        self.transport.close()


class DBmysql(object):
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                                    db=self.database)
        self.cur = self.conn.cursor()

    def exec_sql(self, ):
        sql = 'SELECT host.hostname AS physical FROM grp,grp_host,host ' \
              'WHERE host.id = grp_host.host_id ' \
              'AND grp.id = grp_host.grp_id ' \
              'AND ( grp.grp_name=\'mostly-physical machine\' OR  grp.grp_name=\'mostly-vm\' OR grp.grp_name=\'fastdfs\') ' \
              'GROUP BY host.hostname ;'
        self.cur.execute(sql)
        ip_all_list = []
        for one in self.cur.fetchall():
            ip_all_list.append(one[0])
        return ip_all_list

    def disconnect(self):
        self.conn.close()


def ping_host(ip):
    """对传进来的ip列表进行检查,ping通的ip传入队列"""
    command = "ping -n -i.1 -w 1 %s > /dev/null" % str(ip)
    # print(command)
    ret2 = subprocess.call(command, shell=True)
    # print(ret2)
    if not ret2:
        q.put(ip)


def parse_ip(ip_seg):
    """
    分析出整个网段IP,将ip传入ping_host方法检测.
    然后从队列取出ping通的ip
    """
    ip = IPy.IP(ip_seg)
    ip_list = []
    threads_one = []
    for ping_ip in ip:
        # print(ping_ip)
        if str(ping_ip).endswith(".0") or str(ping_ip).endswith(".255") or str(ping_ip) in exclude_ip:
            continue
        else:
            tt = threading.Thread(target=ping_host, args=(str(ping_ip),))
            threads_one.append(tt)
    for tt in threads_one:
        tt.setDaemon(True)
        tt.start()
    for tt in threads_one:
        tt.join()
    while not q.empty():
        ip_list.append(q.get())
    return ip_list


def PingToList(ssh_channel, ping_command, log_file):
    """传入的命令通过传进来的ssh_channel执行.将结果分析并记入日志"""
    semaphore.acquire()
    res = ssh_channel.cmd(ping_command).decode()
    try:
        re.search("(Unicast.*ms)", res).groups()[0]
    except AttributeError as e:
        semaphore.release()
    else:
        small_res = re.search("(Unicast.*ms)", res).group()
        ip = re.search("((\d{1,3}.)+)", small_res).group()
        mac = re.search("((\w{2}:)+\w{2})", small_res).group()
        ip_mac_log = ip + " " + mac + "\n"
        # print(ip_mac_log)

        with open(log_file, "r") as f:
            # print(f.read())
            all = f.read()
        reg = "(.*" + mac.strip() + ")"
        find_res = re.findall(reg, all)
        # print(find_res)
        if len(find_res) != 0:
            # 定义文件名
            file = basedir + "/mac_mutli_ip/" + mac
            # 清空文件
            with open(file, "w") as a:
                pass
            with open(file, "a+") as mac_file:
                # 把自己写入log
                mac_file.write(ip_mac_log)

                for line in find_res:
                    # 把过滤出来的写入文件.mac地址命名的文件.
                    mac_file.write(line)

        with open(log_file, "a+") as log:
            log.write(ip_mac_log)
        semaphore.release()


def query_db_for_log(ip_log_file):
    """从文件读出所有的ip,循环在ip_all_list查,如果不在就用mac地址文件找..最后返回本网段错误ip列表"""
    with open(ip_log_file, "r") as file:
        all_ip = file.readlines()
    error_ip = []
    for ip_line in all_ip:
        # print(ip_line.split("  "))
        ip = ip_line.split("  ")[0]
        mac = ip_line.split("  ")[1].rstrip("\n")
        # row = mysql_channel.exec_sql(ip)
        if ip not in ip_all_list:
            mac_file_name = basedir + "/mac_mutli_ip/" + mac
            try:
                with open(mac_file_name, "r") as mac_file:
                    mutil_ip = mac_file.readlines()
            except FileNotFoundError as e:
                error_ip.append(ip)
            else:
                for new_ip_line in mutil_ip:
                    m_ip = new_ip_line.split("  ")[0]
                    m_mac = new_ip_line.split("  ")[1].rstrip("\n")
                    if m_ip == ip:
                        continue
                    else:
                        if m_ip in ip_all_list:
                            break
                        else:
                            error_ip.append(m_ip)
    return error_ip


if __name__ == "__main__":
    db_host = db_config["db_host"]
    db_port = db_config["db_port"]
    db_username = db_config["db_username"]
    db_password = db_config["db_password"]
    db_defaultdb = db_config["db_default_db"]
    # print(db_defaultdb)
    mysql_conn = DBmysql(db_host, db_port, db_username, db_password, db_defaultdb)
    # 获取所有falcon存在的ip列表
    ip_all_list = mysql_conn.exec_sql()
    mysql_conn.disconnect()
    # 日志文件列表
    ip_log_file_list = []
    for segment in net_segment.keys():
        print("segment: ", str(segment), " start up")
        # 生成arping需要的ip列表
        segment_ip_list = parse_ip(segment)
        # print(segment_ip_list)
        log_file = basedir + "/%s.log" % segment.__str__().replace("/", "_")
        # 文件加入列表.方便后面分析日志使用.
        ip_log_file_list.append(log_file)
        with open(log_file, "w") as f:
            pass
        remote_host = net_segment[segment]["host"]
        remote_host_interface = net_segment[segment]["interface"]
        segment = SSH(host=remote_host, port=3222, user='root')
        segment.connect()
        semaphore = threading.BoundedSemaphore(5)
        threads = []
        # 多线程ping
        for ip in segment_ip_list:
            ping_command = "arping -f -w 1 -I %s %s" % (remote_host_interface, ip)
            # PingToList(ssh_channel=segment, ping_command=ping_command, log_file=log_file)
            t = threading.Thread(target=PingToList, args=(segment, ping_command, log_file))
            threads.append(t)
        # 开始执行线程里的任务.
        for t in threads:
            t.setDaemon(True)
            t.start()

        # 等待线程里的任务执行完成.
        for t in threads:
            t.join()

    # 读取所有的日志并进入MySQL里面查..如果有就ok.没有就报警
    all_error_ip = []
    for ip_log_file in ip_log_file_list:
        segment_error_ip_list = query_db_for_log(ip_log_file)
        all_error_ip.extend(segment_error_ip_list)
    error_ip_num = len(all_error_ip)
    # 如果有错误ip,就报警.
    headers = {'Host': 'falcondata.xiaqiu.cn', }
    url = "http://192.168.23.238:3222/null--ping_check_host--600--%s--check=ping_host--null" % error_ip_num
    if error_ip_num != 0:
        time_now = time.strftime('%Y_%m_%d-%H:%M', time.localtime(time.time()))
        error_log_path = basedir + config.error_ip_log
        with open(error_log_path, 'a+') as error_log:
            error_log.write(time_now + "\n")
            for err_ip in all_error_ip:
                error_log.write(err_ip + "\n")
                #        print(all_error_ip)

    r = requests.get(url=url, headers=headers)
    # print(r.text)
    print("all done")
