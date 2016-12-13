import threading
import time


def run(n):
    time.sleep(1)
    print(n)


for i in range(10):
    t = threading.Thread(target=run, args=(i,))
    t.start()
