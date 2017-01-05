import pika
import sys

credentails = pika.PlainCredentials("zewei", 'alexdje')  # 认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', credentials=credentails))  # 认证模式
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
