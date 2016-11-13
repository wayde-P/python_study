import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import accounts

info = False
user = "none"
def login(func):
    def inner():
        retry_count = 0
        global info
        global user
        while not info:
            if retry_count < 3 and not info :
                user = input("user: ").strip()
                pwd = input("password: ").strip()
                # name = accounts.load_account_info(user)["id"]
                password = accounts.load_account_info(user)["password"]
                if pwd == password:
                    info = True
                else:
                    retry_count += 1
            else:
                print("重试次数太多")

        if info:
            func(user)
    return inner

