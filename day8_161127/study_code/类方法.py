class Dog(object):
    name = 'dfad'

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" % self.name)


# 类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
d = Dog("ChenRonghua")
d.eat()
