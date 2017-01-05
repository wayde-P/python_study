import pika
import sys

credentails = pika.PlainCredentials("zewei", 'alexdje')  # 认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', credentials=credentails))  # 认证模式
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [binding_key] [*.error.*]\n" % sys.argv[0])
    sys.exit(1)

for binding_key in severities:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
