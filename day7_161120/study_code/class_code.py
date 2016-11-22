class dog(object):
    def __init__(self, name,food):
        self.NAME = name
        self.FOOD = food

    def sayhi(self):
        print("my name is ", self.NAME)

    def eat(self):
        print("wo zhengzai chi " , self.FOOD)


d = dog("lichuang","baozi")
d.sayhi()
d.eat()
