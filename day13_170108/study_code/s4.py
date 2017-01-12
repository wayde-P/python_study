# import memcache
#
# mc = memcache.Client([('10.211.55.4:12000',1),('10.211.55.5:12000',10),('10.211.55.6:12000',5)], debug=True)
# mc.set("foo", "bar")
# ret = mc.get('foo')

import memcache
import time

mc = memcache.Client(['192.168.12.78:12000'], debug=True, cache_cas=True)
# mc.set('product_count',900)
# v = mc.get('product_count')
# print(v)

# 900,1
v = mc.gets('product_count')
# 900
time.sleep(1000)
mc.cas('product_count', "899")
# 899,1
