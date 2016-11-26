import sys
import os
import json

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)


# print(sys.path)

class Operate(object):
    def __init__(self, file_name):
        self.Filename = file_name

    def load_data(self):
        with open(self.Filename) as DB:
            data = json.load(DB)
        return data

    def dump_data(self, data):
        with open(self.Filename, "w+") as DB:
            DB.write(json.dumps(data, DB))
        return "ok"
