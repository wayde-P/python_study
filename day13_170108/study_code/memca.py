import memcache

mc = memcache.Client(['192.168.12.78:12000'], debug=True, cache_cas=True)

# mc.set("zzw",18)
# v = mc.get("zzw")
# print(v)

v = mc.gets('zhangzewei')
mc.cas('zhangzewei', "899")
v = mc.gets('zhangzewei')
print(v)
