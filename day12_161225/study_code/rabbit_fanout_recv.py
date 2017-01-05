import pika, sys

credentails = pika.PlainCredentials("zewei", 'alexdje')  # 认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', credentials=credentails))  # 认证模式
channel = connection.channel()  # 建立通道
channel.exchange_declare(exchange='logs', type='fanout')  # 定义exchange名和广播模式fanout

result = channel.queue_declare(exclusive=True)  # 不指定queue名字.rabbit会自动分配一个queue_name,exclusive=True会在消费者断开后自动将queue删除

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print("waiting for logs ")


def callback(ch, method, properties, body):
    print("[X] %r" % body)


channel.basic_consume(callback, queue=queue_name)
