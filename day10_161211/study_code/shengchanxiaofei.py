import queue, time, threading


def consumer(name):
    while True:
        print("%s get bone %s,and eating" % (name, q.get()))


def producer(name):
    count = 0
    while True:
        print("%s create a shit" % name, count)
        q.put(count)
        count += 1
        time.sleep(3)


q = queue.Queue()
p1 = threading.Thread(target=producer, args=("zewei",))
p2 = threading.Thread(target=producer, args=("lili",))
p1.start()
c1 = threading.Thread(target=consumer, args=("lili",))
c1.start()
