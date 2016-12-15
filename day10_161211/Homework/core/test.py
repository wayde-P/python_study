import optparse
import configparser
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

config = configparser.ConfigParser()
config.read(settings.host_file)
config.read(settings.group_file)
all_server = config.sections()
print(config['192.168.1.1']['user'])
for i in config['webserver']:
    print(i)

print(all_server)
