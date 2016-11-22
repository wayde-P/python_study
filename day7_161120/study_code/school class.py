class SchoolMember(object):
    '''学校基类
    初始化成员信息
    '''
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        print("just enrolled new person ", self.name)
        SchoolMember.member += 1

    def tell(self):
        for k, v in self.__dict__.items():
            print(k, v)

    def __del__(self):
        print("开除了", self.name)


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course, salary):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.salary = salary
        # SchoolMember.tell(self)


class Student(SchoolMember):
    def __init__(self, name, age, sex, tuition, course):
        # SchoolMember.__init__(self,name,age,sex)
        super(Student, self).__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print("ganggang 交了 ", self.tuition)
        self.amount += amount
