import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.50.136'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
