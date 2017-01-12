import memcache
import time

mc = memcache.Client(['192.168.12.78:12000'], debug=True, cache_cas=True)
# 900,1
v = mc.gets('product_count')
mc.cas('product_count', "899")
# 899,1
# 899,2
