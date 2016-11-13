import sys
import os

print(len(sys.argv))
if len(sys.argv) < 3:
    print("eg:\n\t", sys.argv[0], "old_str new_str filename")
    exit()

source = open(sys.argv[3], encoding='utf-8')
new_file = open("temple", "w+", encoding='utf-8 ')
while True:
    data = source.readline()
    data = data.replace(sys.argv[1], sys.argv[2])
    new_file.write(data)
    print(data)
    if len(data) == 0:
        break
source.close()
new_file.close()
os.remove(sys.argv[3])
os.rename("temple", sys.argv[3])
