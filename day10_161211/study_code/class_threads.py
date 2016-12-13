import time, threading


class Mythread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("run,aaaa", self.num)
        time.sleep(1)


if __name__ == "__main__":
    t1 = Mythread(1)
    t2 = Mythread(2)
    t1.start()
    t2.start()
