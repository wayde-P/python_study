import pika
import sys

credentails = pika.PlainCredentials("zewei", 'alexdje')  # 认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', credentials=credentails))  # 认证模式
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
