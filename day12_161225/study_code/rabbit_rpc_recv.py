import pika
import time
import subprocess

credentials = pika.PlainCredentials('zewei', 'ZZW')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.50.136', credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='rpc_queue3')


def SSHRPCServer(cmd):
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)
    print("recv cmd:", cmd)
    cmd_obj = subprocess.Popen(cmd.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    result = cmd_obj.stdout.read() or cmd_obj.stderr.read()
    return result


def on_request(ch, method, props, body):
    # n = int(body)

    print(" [.] fib(%s)" % body)
    response = SSHRPCServer(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=response)


channel.basic_consume(on_request, queue='rpc_queue3')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
