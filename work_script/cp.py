import os
import subprocess

work_dir = '/home/vmail/ttxrw.com/'

os.chdir(work_dir)
command = "rsync -av tom1 test"
subprocess.Popen("command",shell=True)
#shutil.copytree("tom1","test",ignore="*,s")