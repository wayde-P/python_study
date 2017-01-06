import pika
import uuid


class SSHRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('alex', 'alex3714')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='192.168.50.136', credentials=credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)  # 客户端的结果必须要返回到这个queue
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, queue=self.callback_queue)  # 声明从这个queue里收结果

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  # 任务标识符
            self.response = body
            print(body)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())  # 唯一标识符
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue3',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        #
        print("start waiting for cmd result")
        # self.channel.start_consuming()
        count = 0
        while self.response is None:  # 如果命令没返回结果
            print("loop ", count)
            count += 1
            self.connection.process_data_events()  # 以不阻塞的形式去检测有没有新事件
            # 如果没事件，那就什么也不做， 如果有事件，就触发on_response事件
        return self.response


ssh_rpc = SSHRpcClient()

print(" [x] sending cmd")
response = ssh_rpc.call("ipconfig")

print(" [.] Got result ")
print(response.decode("gbk"))
