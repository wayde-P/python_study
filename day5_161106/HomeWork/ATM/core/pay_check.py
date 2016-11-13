import os

pay_list_path = "%s/logs" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pay_list(user):
    pay_abspath = "%s/%s.pay" % (pay_list_path, user)
    # print(pay_abspath)
    if os.path.exists(pay_list_path):
        with open(pay_abspath) as r_file:
            data = r_file.readlines()
            for i in data:
                print(i)



# pay_list("jerry")