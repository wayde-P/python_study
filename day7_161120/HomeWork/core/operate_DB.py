import sys
import os
import json

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)


# print(sys.path)

class Operate(object):
    Filename = "%s/db/DB.json" % basedir

    # def __init__(self):
    #     self.Filename = "%s/db/DB.json" % basedir

    def load_data(self):
        with open(Filename) as DB:
            data = json.load(DB)
        return data

    def dump_data(self, data):
        with open(Filename, "w+") as DB:
            DB.write(json.dumps(data, DB))
        return "ok"
