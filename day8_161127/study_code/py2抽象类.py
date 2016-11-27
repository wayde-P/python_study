import abc
# 调用抽象类.如果子类没有实现父类的方法 222222222222223333333333就报错raise ....

class Alert(object):
    '''报警基类'''
    # __metaclass__ = abc.ABCMeta
    #
    # @abc.abstractmethod
    def send(self):
        '''报警消息发送接口'''
        raise NotImplementedError


class MailAlert(Alert):
    pass


m = MailAlert()
m.send()