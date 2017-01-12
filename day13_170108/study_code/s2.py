import redis

# 创建连接
conn = redis.Redis(host='192.168.12.78')
# 创建订阅者
pub = conn.pubsub()
# 订阅频道
pub.subscribe('fm104.8')
# pub.parse_response()

while True:
    # 去频道中获取消息（hang主）
    msg = pub.parse_response()
    print(msg)
