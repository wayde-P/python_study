import redis

redis = redis.Redis(host='192.168.50.129', port=6379)

redis.set('zhang', 'zewei')
b = redis.get('zhang')
print(b)
