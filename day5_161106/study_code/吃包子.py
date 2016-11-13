import time


def chihuo(name):
    print("%s准备吃包子"% name)
    while True:
        baozi = yield
        print("包子 %s 来了.被 %s 吃了"%(baozi,name))

def kook():
    c = chihuo("A")
    c1 = chihuo("b")
    c2 = chihuo("c")
    next(c)
    next(c1)
    next(c2)
    for i in range(10):
        time.sleep(1)
        print("做3个包子")
        c.send(i)
        c1.send(i)
        c2.send(i)

kook()


def print_hello(name):
    print("%s say hello!"% name)

a="jerry"

print_hello("herry")



