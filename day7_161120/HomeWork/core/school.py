import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import operate_DB
from core import course


class School(object):
    def __init__(self, address):
        # self.Course = course.Course()
        self.load_data = operate_DB.Operate.load_data(self)
        self.dump_data = operate_DB.Operate
        self.Address = address

    def create_school(self):
        self.load_data["学校"][self.Address] = {}
        return self.Address

    # def create_course(self, name, period, price):  # 创建课程,代入周期和价格参数
    #     self.Price = price
    #     self.Period = period
    #     self.Name = name
    #     self.Course.create_course(self.Name, self.Period, self.Price)

    def show_school(self):
        data = self.load_data["学校"].keys()
        return data


a = School("guangzhou")
a.create_school()
