import threading
import time

event = threading.Event()


def ligher():
    count = 0
    while True:
        if count < 30:
            if not event.is_set():
                event.set()
            print("gree light")
        elif count < 34:
            print("yellow light")
        elif count < 60:
            print("red light")
            event.clear()
        else:
            count = 0
        count += 1
        time.sleep(0.2)


def car(n):
    count = 0
    while True:
        event.wait()
        print("car is running...")
        time.sleep(0.3)


light = threading.Thread(target=ligher)
light.start()

c1 = threading.Thread(target=car, args=(1,))
c1.start()
