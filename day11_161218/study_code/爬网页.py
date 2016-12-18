import gevent
from gevent import monkey

monkey.patch_all()
from  urllib.request import urlopen
import time


def pa_web_page(url):
    print("GET url", url)
    req = urlopen(url)
    data = req.read()
    print(data)
    print('%d bytes received from %s.' % (len(data), url))


t_start = time.time()
pa_web_page("http://www.autohome.com.cn/beijing/")
pa_web_page("http://www.xiaohuar.com/")
print("time cost:", time.time() - t_start)

t2_start = time.time()
gevent.joinall([
    # gevent.spawn(pa_web_page, 'https://www.python.org/'),
    gevent.spawn(pa_web_page, 'http://www.autohome.com.cn/beijing/'),
    gevent.spawn(pa_web_page, 'http://www.xiaohuar.com/'),
    # gevent.spawn(pa_web_page, 'https://github.com/'),
])
print("time cost t2:", time.time() - t2_start)
