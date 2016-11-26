import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

# print(sys.path)
from core import operate_DB


class Course(object):
    def __init__(self):
        self.OPerate_DB = operate_DB.Operate("%s/db/Course.json" % basedir)

    def create_course(self, name, period, price):
        data = self.OPerate_DB.load_data()
        data[name] = {"peroid": period, "price": price}
        self.OPerate_DB.dump_data(data)

    def show_course(self):
        data = self.OPerate_DB.load_data()
        return data
