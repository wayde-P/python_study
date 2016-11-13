import os
import sys

ATM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ATM)

from core import accounts
from core import transaction
from core import pay_check
from core import auth


# global user
@auth.login
def account_info(user):

    print(accounts.load_account_info(user))

@auth.login
def repay(user):
    repay_money = int(input("请输入还款数: ").strip())
    transaction.make_transaction("repay", user, repay_money)

@auth.login
def withdraw(user):
    withdraw_money = int(input("请输入取现金额: ").strip())
    transaction.make_transaction("withdraw", user, withdraw_money)

@auth.login
def transfer(user):
    transfer_money = int(input("请输入转入金额: ").strip())
    transfer_to = input("转给谁:").strip()
    transaction.make_transaction("transfer", user, transfer_money,transfer_to)

@auth.login
def pay_a(user):
    pay_check.pay_list(user)


def logout():
    exit("bye bye ! 欢迎下次光临!")


def interactive():
    """
    interact with user
    :return:
    """
    menu = '''
    ------- zewei Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_a,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # user=input("username:")
            menu_dic[user_option]()

        elif len(user_option) == 0 :
            continue
        else:
            print("\033[31;1mOption does not exist!\033[0m")

interactive()


# def run():
#     '''
#     this function will be called right a way when the program started, here handles the user interaction stuff
#     :return:
#     '''
#     acc_data = auth.acc_login(user_data, access_logger)
#     if user_data['is_authenticated']:
#         user_data['account_data'] = acc_data
#         interactive(user_data)
