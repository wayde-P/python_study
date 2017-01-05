import pika, sys

credentails = pika.PlainCredentials("zewei", 'alexdje')  # 认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', credentials=credentails))  # 认证模式
channel = connection.channel()  # 建立通道
channel.exchange_declare(exchange='logs', type='fanout')  # 定义exchange名和广播模式fanout
message = ' '.join(sys.argv[1:]) or "info: hello world"

channel.basic_publish(exchange='logs', routing_key='', body=message)  # 给exchange发送信息
print(message, " sent ")
