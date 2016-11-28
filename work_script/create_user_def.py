import pymysql
import os
import subprocess
import time
from random import Random

mysql_host = "192.168.0.34"
mysql_port = 3306
mysql_user = "postfix"
mysql_password = "postfix"
mysql_db = "postfix"
mysql_charset = "UTF8"

work_dir = '/home/vmail/ttxrw.com/'

conn = pymysql.connect(host=mysql_host,
                       port=mysql_port,
                       user=mysql_user,
                       password=mysql_password,
                       db=mysql_db,
                       charset=mysql_charset
                       )


def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


cur = conn.cursor()
date = "ttxrw.%s" % time.strftime("%Y%m%d", time.localtime())
num = int(input("input create mail number:").strip())
with open(date, "w+") as name_list:
    for i in range(num):
        user_name = random_str()
        domain_name = "ttxrw.com"
        mail_name = user_name + "@" + domain_name
        directory = domain_name + "/" + user_name + "/"
        sql1 = "insert into alias (address,domain,goto,created,modified,active) VALUES ('%s','%s','%s',now(),now(),'1');" % \
               (mail_name, domain_name, mail_name)
        sql2 = "INSERT INTO mailbox " \
               "(username,local_part,domain,maildir,password,name,quota,active,created,modified) " \
               "VALUES " \
               "('%s','%s','%s','%s','{CRAM-MD5}ee1f78573314f6c9099cc18e184d75b9ea6e7e6f4ce7ebf5fc4d2d12a95c0cac','%s','0','1',now(),now());" \
               % (mail_name, user_name, domain_name, directory, user_name)

        cur.execute(u"{0:s}".format(sql1))
        cur.execute("%s" % sql2)
        command = "rsync -av --exclude='*,S' --delete tom1/ %s/" % user_name
        subprocess.Popen(command, shell=True, cwd=work_dir)
        name_list.write(user_name+"\n")
    cur.close()
    conn.close()