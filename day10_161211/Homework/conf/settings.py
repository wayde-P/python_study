import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
host_file = "%s/host.cfg" % BASE_DIR
group_file = "%s/group.cfg" % BASE_DIR
