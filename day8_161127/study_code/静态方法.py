class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 把eat方法变为静态方法
    def eat(self):
        print("%s is eating" % self.name)

# 静态方法的方法和类本身已经没有什么关系了.既不能访问类变量.也不能访问实例变量

d = Dog("ChenRonghua")
d.eat(d)