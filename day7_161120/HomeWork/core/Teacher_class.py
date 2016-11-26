import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import operate_DB


class Teacher(object):
    def __init__(self, name, address, course):
        self.operate_DB = operate_DB.Operate("%s/db/Teacher.json" % basedir)
        self.address = address
        self.course = course
        self.name = name

    def create_class(self):
        pass

    def show_teacher(self):
        pass
