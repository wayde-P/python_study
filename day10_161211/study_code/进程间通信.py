import multiprocessing as mp
import time


def f(q):
    q.put([22, None, "hello"])
    time.sleep(3)


if __name__ == "__main__":
    q = mp.Queue()
    p = mp.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
    print("p over")
