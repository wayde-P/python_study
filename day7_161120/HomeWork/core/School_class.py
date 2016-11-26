import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import Course_class
from core import operate_DB


class School(object):
    def __init__(self, address):
        self.Course = Course_class.Course()
        self.operate_DB = operate_DB.Operate("%s/db/School.json" % basedir)
        self.Address = address

    def create_school(self, course_name, teacher_name):
        return self.Address

    def create_course(self, name, period, price):  # 创建课程,代入周期和价格参数
        self.Price = price
        self.Period = period
        self.Name = name
        self.Course.create_course(self.Name, self.Period, self.Price)

    def show_school(self):
        data = self.operate_DB.load_data()
        return data

#
# a = School("beijing")
# print(a.create_school())
# a.create_course("python",6,45444)
