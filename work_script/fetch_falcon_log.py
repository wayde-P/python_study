import json
import os
import datetime

basedir = os.path.dirname(os.path.abspath(__file__))
year = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y')
month = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%m').lstrip('0')
day = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d').lstrip('0')
yesterday = "%s-%s-%s" % (year, month, day)

log_file = basedir + '/logs/' + yesterday + '.log'

with open(log_file, "r") as source_log_file:
    source_log_lines = source_log_file.readlines()

error_dict = {}
for log_line in source_log_lines:
    if log_line == "\n":
        continue
    else:
        line_time = log_line.split("=>")[0]
        line_json_log = log_line.split("=>")[1].rstrip("\n")
        line_dict = json.loads(line_json_log)
        if line_dict["status"] == "OK":
            continue
        else:
            host_ip = line_dict["endpoint"]
            leftValue = line_dict["leftValue"]
            metric_name = line_dict["strategy"]["metric"]
            # print("host ip %s ,leftValue %s , metric_name: %s " % (host_ip, leftValue, metric_name))
            if not error_dict.get(host_ip):
                error_dict[host_ip] = {}
            if not error_dict[host_ip].get(metric_name):
                error_dict[host_ip][metric_name] = {}
                error_dict[host_ip][metric_name]["count"] = 1
                error_dict[host_ip][metric_name]["avg_leftValue"] = leftValue
            else:
                error_dict[host_ip][metric_name]["count"] += 1
                error_dict[host_ip][metric_name]["avg_leftValue"] += leftValue

# print(error_dict)

for host, a in error_dict.items():
    for metric, b in error_dict[host].items():
        for item, value in error_dict[host][metric].items():
            if item == "avg_leftValue":
                avg_count = error_dict[host][metric]["count"]
                avg_leftValue = value / error_dict[host][metric]["count"]
            else:
                continue
            print(host, error_dict[host][metric]["count"], metric, '%5.3F' % avg_leftValue)
