import pika
import uuid
import time
from random import Random


class SSHRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('zewei', 'ZZW')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.50.136', credentials=credentials))
        self.channel = self.connection.channel()
        # self.corr_id = corr_id
        result = self.channel.queue_declare(exclusive=True)  # 客户端的结果必须要返回到这个queue
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, queue=self.callback_queue)  # 声明从这个queue里收结果

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  # 任务标识符
            self.response = body
            print(body.decode("gbk"))

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())  # 唯一标识符
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue3',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,  # 返回到哪个queue里面
                                   ),
                                   body=str(n))
        #

    def get_respones(self):
        print("start waiting for cmd result")
        # self.channel.start_consuming()
        count = 0
        while self.response is None:  # 如果命令没返回结果
            print("loop ", count)
            time.sleep(0.1)
            count += 1
            self.connection.process_data_events()  # 以非阻塞的形式去检测有没有新事件
            # 如果没事件，那就什么也不做， 如果有事件，就触发on_response事件
        return self.response


def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


task_dict = {}
while True:
    c_input = str(input(">>").strip())

    if c_input.startswith('run'):
        # if c_input:
        run_dict = {
            'run': [],
            '--host': []
        }
        tag = False
        for a in c_input:
            if tag and a in run_dict:
                tag = False
            if not tag and a in run_dict.keys():
                tag = True
                key = a
                continue
            if tag:
                run_dict[key].append(a)

        task_id = random_str()
        task_dict[task_id] = SSHRpcClient()
        task_dict[task_id].call(c_input)
        for i in task_dict.keys():
            print("task id :", i)

    elif c_input.startswith('check_task'):
        lis = c_input.split()
        task_dict[lis[-1]].get_respones()

    elif len(c_input) == 0:
        continue
