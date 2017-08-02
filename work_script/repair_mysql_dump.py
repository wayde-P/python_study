#!/bin/env python3
import time
import sys
import subprocess

print(len(sys.argv))
if len(sys.argv) < 7:
    print("eg:\n\t", sys.argv[0], "db_ip db_port db_name db_part_tbale db_part_key hive_db_name")
    exit()
else:
    db_ip = sys.argv[1]
    db_port = sys.argv[2]
    db_name = sys.argv[3]
    db_part_tbale = sys.argv[4]
    db_part_key = sys.argv[5]
    hive_db_name = sys.argv[6]


def fetch_time(oldtime):
    # old_time = "2017/4/5 14:30:00"
    a = time.strptime(oldtime, "%Y-%m-%d %H:%M:%S")
    print(time.mktime(a))
    b = time.mktime(a) + 28800 + 1800
    # print("geshihua",a,"\n",b)
    # print("gmtime",time.gmtime(b))
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(b))
    pathvalue = time.strftime("%Y%m%d-%H%M", time.gmtime(b))
    path_time = time.strftime("%H%M", time.gmtime(b))
    file_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime(b))

    time_list = []
    time_list.append(current_time)
    time_list.append(pathvalue)
    time_list.append(path_time)
    time_list.append(file_time)

    return time_list
    # print(a.split(".")[0])


start_time = str("2016-11-01 09:00:00")
end_time = str("2017-07-17 17:30:00")
# end_time = str("2017-05-09 14:30:00")
# end_time = str("1494311400.0")


while start_time != end_time:
    time_list = fetch_time(start_time)
    current_time = time_list[0]
    pathvalue = time_list[1]
    path_time = time_list[2]
    file_time = time_list[3]
    print("start_time: ", start_time)
    print("current_time: ", current_time)

    bak_path = "mkdir -p /opt/db-backup/partition-sql-bk/{hive_db_name}/{pathvalue}" \
        .format(hive_db_name=hive_db_name, pathvalue=pathvalue)
    mkdir_process = subprocess.Popen(bak_path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
    mkdir_process.communicate()
    cmd = "/opt/mysql/bin/mysqldump -uhadoop -phdp@7689 -h {db_ip} -P {db_port} -w" \
          " \"{db_part_key} >= '{start_time}' and {db_part_key} < '{current_time}';\"" \
          " --skip-tz-utc --single-transaction --flush-logs --master-data=2 " \
          "{db_name} {db_part_tbale} >> /opt/db-backup/partition-sql-bk/" \
          "{hive_db_name}/{pathvalue}/{hive_db_name}.{db_part_tbale}.{file_time}.sql".format \
        (db_ip=db_ip, db_port=db_port, db_part_key=db_part_key, start_time=start_time, current_time=current_time,
         db_name=db_name, db_part_tbale=db_part_tbale, hive_db_name=hive_db_name, pathvalue=pathvalue,
         file_time=file_time)
    print(cmd)
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate()
    time.sleep(1)
    start_time = current_time

    # demeter_etl/20170717-1630/demeter_etl.demeter_comment.2017-07-17.16\:30\:01.sq
