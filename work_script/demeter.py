#!/bin/env python3
import time
import subprocess

start_time = str("2017-05-17 13:30:00")
end_time = str("2017-05-17 14:00:00")

table_list = ["demeter_credit"]


# table_list = ["demeter_bankcard", "demeter_bankcard_history", "demeter_borrow",
#               "demeter_borrow_history",
#               "demeter_career", "demeter_comment", "demeter_contact", "demeter_credit_blacklist",
#               "demeter_credit_history",
#               "demeter_id", "demeter_product", "demeter_user"]
# table_list = ["demeter_credit", "demeter_bankcard", "demeter_bankcard_history", "demeter_borrow",
#               "demeter_borrow_history",
#               "demeter_career", "demeter_comment", "demeter_contact", "demeter_credit_blacklist",
#               "demeter_credit_history",
#               "demeter_id", "demeter_product", "demeter_user"]


def fetch_time(oldtime):
    # oldtime = "2017/4/5 14:30:00"
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


while start_time != end_time:
    time_list = fetch_time(start_time)
    current_time = time_list[0]
    pathvalue = time_list[1]
    path_time = time_list[2]
    log_time = time_list[3]
    print("start_time: ", start_time)
    print("current_time: ", current_time)
    for i in table_list:
        cmd = "sh /opt/db-backup/hive-partition/tohive_part_v1.1_zewei.sh " \
              "{0}  " \
              "create \"{1}\" \"{2}\" \"{3}\" \"{4}\"" \
              " 1>/tmp/log/db_backup/{0}.{5}.log 2>/tmp/log/db_backup/{0}.{5}.log".format(
            i, pathvalue, path_time, start_time, current_time, log_time
        )
        print(cmd)
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        process.communicate()
        time.sleep(2)
    start_time = current_time
