import gevent


def func1():
    print('\033[31;1mli and hai\033[0m')
    gevent.sleep(2)
    print('\033[31;1mli youqu and hai\033[0m')


def func2():
    print('\033[32;1mli qiehuan and long\033[0m')
    gevent.sleep(1)
    print('\033[32;1mlichang gao wan haito\33[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])
