import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from core import operate_DB


class classes(object):
    def __init__(self):
        self.OPerate_DB = operate_DB.Operate("%s/db/classes.json" % basedir)

    def crete_class(self, name, address, course):
        data = self.OPerate_DB.handle_data()
        data[name] = {"address": address, "course": course}
        self.OPerate_DB.dump_data(data)
