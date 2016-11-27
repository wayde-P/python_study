class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("wanm...wagn...wang")


class blackperson(person):
    def __init__(self, name, age, strength):
        person.__init__(self, name, age)
        self.strength = strength

    def talk(self):
        print("%s is walking.." % self.name)


b = blackperson("zewei", 22, "niu")
print(b)
