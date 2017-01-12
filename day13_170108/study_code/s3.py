import redis

conn = redis.Redis(host='192.168.12.78')
conn.publish('fm104.8', '报警了。。。')
