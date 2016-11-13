import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

# 打印当前余额并让用户偿还账单

from core import accounts
from core import money_check
from conf import settings
from core import logger


def make_transaction(tran_type, account, money, *in_account):
    account_info = accounts.load_account_info(account)  # 取出用户的信息
    currten_blance = account_info["balance"]  # 获取剩余的钱
    interest = settings.TRANSACTION_TYPE[tran_type]['interest']
    if tran_type in settings.TRANSACTION_TYPE:
        if tran_type == 'repay':  # 还钱
            new_blance = currten_blance + money - interest  # 剩余的钱加上还的钱
            account_info["balance"] = new_blance
            print("当前余额为 %s, 还款后余额为 %s." % (currten_blance, new_blance))
            accounts.update_accout_info(account_info)  # 更新账号信息
        elif tran_type == 'consume':  # 消费接口
            if money_check.pay_check(account, money):
                new_blance = currten_blance - money - interest
                account_info["balance"] = new_blance
                print("当前余额为 %s, 消费后余额为 %s." % (currten_blance, new_blance))
                accounts.update_accout_info(account_info)  # 更新账号信息
            else:
                money_check.pay_check(account, money)
                print("钱不够,请还钱....")
                return False
        elif tran_type == 'withdraw':  # 取现
            withdraw_currten_blance = account_info["balance"] / 2
            if money > withdraw_currten_blance:
                print("取现的额度不能大于剩余额度的50%")
                return False
            elif money <= withdraw_currten_blance:
                new_blance = currten_blance - money - interest
                account_info["balance"] = new_blance
                print("当前余额: %s, 取现后余额为: %s 手续费: %s." % (currten_blance, new_blance, interest))
                accounts.update_accout_info(account_info)  # 更新账号信息
        elif tran_type == 'transfer':  # 转账
            out_user = account
            in_user = in_account[0]
            if money_check.pay_check(out_user, money):
                out_user_info = accounts.load_account_info(out_user)  # 读取转出用户的信息
                in_user_info = accounts.load_account_info(in_user)  # 读取转入用户的信息
                out_currten_blance = out_user_info["balance"]  # 获取转出用户的钱数
                out_user_new_blance = out_currten_blance - money  # 转出账号减钱
                in_currten_balnce = in_user_info["balance"]  # 获取转入用户的钱数
                in_user_new_blance = in_currten_balnce + money  # 转入账号加钱
                out_user_info["balance"] = out_user_new_blance  # 重新定义转出账号信息
                in_user_info["balance"] = in_user_new_blance  # 重新定义转入账号信息
                print("%s 账户余额 %s, %s 账户余额 %s" % (out_user, out_user_new_blance, in_user, in_user_new_blance))
                accounts.update_accout_info(out_user_info)  # 写入文件
                accounts.update_accout_info(in_user_info)  # 写入文件
            else:
                money_check.pay_check(account, money)
                print("我在transaction的transfer,钱不够")
                return False
        logger.transaction(tran_type, account, money, interest, *in_account)
        return True
    else:
        print("不支持此类型的消费.")
        return False


# make_transaction("transfer","tom",2000,"jerry")