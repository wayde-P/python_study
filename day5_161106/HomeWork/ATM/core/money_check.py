import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import accounts

def pay_check(account,money):
    current_money = accounts.load_account_info(account)["balance"]
    if money <= current_money:
        return True
    else:
        return False
