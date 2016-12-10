import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

# from core import School_class
from core import operate_DB


class Student(object):
    def __init__(self, name, tuition, grade=0):
        self.OPerate_DB = operate_DB.Operate("%s/db/Student.json" % basedir)
        self.tuition = tuition
        self.grade = grade
        self.name = name

    def create_student(self):
        data = self.OPerate_DB.load_data()
