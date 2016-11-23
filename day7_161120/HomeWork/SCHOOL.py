class School(object):
    def __init__(self, address):
        self.address = address

    def create_class(self, course, teacher):
        pass

    def pay_tuition(self):
        pass

    def create_course(self, period, price):
        pass


class Teacher(School):
    def __init__(self, address):
        super(School, self).__init__(address)


class Student(School):
    tuition = 0

    def __init__(self, address):
        # School.__init__(self, address)
        super(School, self).__init__(address)
