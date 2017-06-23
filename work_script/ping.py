import paramiko
import IPy
import os
import sys
import config
import re
import threading
import subprocess
import queue

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

net_segment = config.config
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


def ping_host(ip):
    command = "ping -n -i.1 -w 1 %s > /dev/null" % str(ip)
    # print(command)
    ret2 = subprocess.call(command, shell=True)
    # print(ret2)
    if not ret2:
        q.put(ip)


def parse_ip(ip_seg):
    # Éú³ÉipµØÖ·ÁÐ±í
    ip = IPy.IP(ip_seg)
    ip_list = []
    threads_one = []
    for ping_ip in ip:
        # print(ping_ip)
        if str(ping_ip).endswith(".0") or str(ping_ip).endswith(".255"):
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
        print(find_res)
        if len(find_res) != 0:
            with open(mac, "a+") as mac_file:
                mac_file.write(ip_mac_log)
                for line in find_res:
                    mac_file.write(line)
                    # print(line)
                    # ip, mac = line.split("  ")
                    # print(ip, "fff", mac)

        with open(log_file, "a+") as log:
            log.write(ip_mac_log)
        semaphore.release()


if __name__ == "__main__":
    for segment in net_segment.keys():
        # 生成arping需要的ip列表
        segment_ip_list = parse_ip(segment)
        # print(segment_ip_list)
        log_file = "%s.log" % segment.__str__().replace("/", "_")
        with open(log_file, "w") as f:
            pass
        remote_host = net_segment[segment]["host"]
        remote_host_interface = net_segment[segment]["interface"]
        segment = SSH(host=remote_host, port=3222, user='root')
        segment.connect()
        semaphore = threading.BoundedSemaphore(5)
        threads = []
        for ip in segment_ip_list:
            ping_command = "arping -f -w 1 -I %s %s" % (remote_host_interface, ip)
            # PingToList(ssh_channel=segment, ping_command=ping_command, log_file=log_file)
            t = threading.Thread(target=PingToList, args=(segment, ping_command, log_file))
            threads.append(t)

        for t in threads:
            t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()
        print("segment: ", str(segment), " done")

    print("all done")
