import os
import sys

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

USER_HOME = "%s/home" % Base_dir

LOG_DIR = "%s/log" % Base_dir
LOG_LEVEL = "DEBUG"

ACCOUNT_DIR = "%s/DB" % Base_dir

HOST = "0.0.0.0"
PORT = 9999
