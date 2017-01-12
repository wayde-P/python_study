import redis

pool = redis.ConnectionPool(host='192.168.12.78', port=6379)

conn = redis.Redis(connection_pool=pool)
# r.set('foo', 'Bar')
# r.get('foo')

# conn.set()
# conn.setnx()

# for i in "海涛":
#     print(i)
# conn.set('hailong','海涛爽妹李闯')
# v = conn.getrange('hailong',0,2)
# print(v,type(v))
# # print(str(v,encoding='utf-8'))
# conn.hscan_iter
# conn.sadd('val1',1,2,3,4,5,6)
# conn.sadd('val2',5,6,7,8)
# v = conn.sunion('val1','val2')
# print(v)

# v = conn.sinter('val1','val2')
# print(v)
