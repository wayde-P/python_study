import json
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from conf import settings


def load_account_info(accout_name):
    db_path = settings.DATABASE["path"]  # 获取db路径
    accout_file = "%s/%s.json" % (db_path, accout_name)
    with open(accout_file) as accout_info:
        account_data = json.load(accout_info)
    return account_data


def update_accout_info(account_data):
    db_path = settings.DATABASE["path"]  # 获取db路径
    accout_file = "%s/%s.json" % (db_path, account_data["id"])
    with open(accout_file, "w") as write_file:
        json.dump(account_data, write_file)
    return True


# print(load_account_info("jerry"))
