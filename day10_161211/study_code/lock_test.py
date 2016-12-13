import threading
import time


def run(n):
    global num
    l.acquire()
    num += 1
    time.sleep(1)
    l.release()
    print(num)
    time.sleep(1)
    # print("thread",n)


l = threading.Lock()
num = 0
t_list = []
for i in range(10):
    t = threading.Thread(target=run, args=(i,))
    t.setDaemon(True)
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print("--main thread---")
print(num)
