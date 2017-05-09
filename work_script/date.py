#!/bin/env python3
import time
import subprocess


def fetch_time(oldtime):
    # old_time = "2017/4/5 14:30:00"
    a = time.strptime(oldtime, "%Y-%m-%d %H:%M:%S")
    print(time.mktime(a))
    b = time.mktime(a) + 28800 + 1800
    # print("geshihua",a,"\n",b)
    # print("gmtime",time.gmtime(b))
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(b))
    pathvalue = time.strftime("%Y%m%d", time.gmtime(b))
    path_time = time.strftime("%H%M", time.gmtime(b))
    log_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime(b))

    time_list = []
    time_list.append(current_time)
    time_list.append(pathvalue)
    time_list.append(path_time)
    time_list.append(log_time)

    return time_list
    # print(a.split(".")[0])


start_time = str("2017-04-05 14:30:00")
end_time = str("2017-04-05 15:00:00")
# end_time = str("2017-05-09 14:30:00")
# end_time = str("1494311400.0")


while start_time != end_time:
    time_list = fetch_time(start_time)
    current_time = time_list[0]
    pathvalue = time_list[1]
    path_time = time_list[2]
    log_time = time_list[3]
    print("start_time: ", start_time)
    print("current_time: ", current_time)
    cmd = "sh /opt/db-backup/hive-partition/tohive_part1.sh " \
          "192.168.22.194 orion " \
          "orion_stat_log orion_part_tmp " \
          "nocreate \"%s\" \"%s\" \"%s\" \"%s\" " \
          " 1>/tmp/log/db_backup/orion_part_%s.log 2>/tmp/log/db_backup/orion_part_%s.log" % (
              start_time, current_time, pathvalue, path_time, log_time, log_time)
    print(cmd)
    # process = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # process.communicate()
    # time.sleep(10)
    start_time = current_time
