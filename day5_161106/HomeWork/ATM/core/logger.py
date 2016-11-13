import os
import time

pay_list_path = "%s/logs" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def transaction(tran_type, account, money, interest=0, *in_account):
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user_pay_list = "%s/%s.pay" % (pay_list_path, account)
    if os.path.exists(user_pay_list):
        if len(in_account) == 0:
            with open(user_pay_list, "a+") as write_file:
                data = "%s\t%s\t%s\t%s\t%s\n" % (date, account, tran_type, money, interest)
                write_file.write(data)
        else:
            with open(user_pay_list, "a+") as write_file:
                data = "%s\t%s\t%s\t%s\t%s\ttrans_to:%s\n" % (date, account, tran_type, money, interest, in_account[0])
                write_file.write(data)
    else:
        if len(in_account) == 0:
            with open(user_pay_list, "a+") as write_file:
                data = "%s\t%s\t%s\t%s\t%s\n" % (date, account, tran_type, money, interest)
                write_file.write(data)
        else:
            with open(user_pay_list, "a+") as write_file:
                data = "%s\t%s\t%s\t%s\t%s\ttrans_to:%s\n" % (date, account, tran_type, money, interest, in_account[0])
                write_file.write(data)
    return True