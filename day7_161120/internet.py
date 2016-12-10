import pickle, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据地址
__db_main = BASE_DIR + r"\main_dict"
__db_teacher = BASE_DIR + r"\teacher_dict"


class School(object):
    # 创建学校
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print("学校名：【%s】\t地址：【%s】" % (self.name, self.addr))

    def hire_teacher(self, dict, course, teacher, file):
        # 数据库添加讲师信息
        dict[self][course] = {"teacher": teacher}
        file_oper(file, "wb", dict)

    def create_course(self, dict, course, file):
        # 数据库添加课程资料
        dict[self][course] = {}
        file_oper(file, "wb", dict)

    def create_grade(self, dict, teacher_dict, course, grade, teacher, file1, file2):
        # 数据库添加班级信息
        dict[self][course]["grade"] = grade
        file_oper(file1, "wb", dict)
        teacher_dict[teacher] = {"grade": grade}
        file_oper(file2, "wb", teacher_dict)


class Course():
    # 创建课程
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        # 查看课程信息
        print("课程：【%s】\t价格：【￥%s】\t周期：【%s个月】"
              % (self.name, self.price, self.time))


class Grade():
    # 创建班级
    def __init__(self, name, course, teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = student

    def cat_grade(self):
        # 查看班级信息
        print("班级：【%s】\t课程：【%s】\t讲师：【%s】"
              % (self.name, self.course, self.teacher))

    def add_student(self, student_name, dict, teacher, file):
        self.student.add(student_name)
        dict[teacher] = {"grade": self}
        file_oper(file, "wb", dict)


class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(People):
    # 创建讲师
    def __init__(self, name, age, school, course, role="讲师"):
        super(Teacher, self).__init__(name, age)
        self.role = role
        self.school = school
        self.course = course

    def cat_teacher(self):
        # 查看老师资料和课程
        print('课程【%s】\t讲师【%s】' % (self.course, self.name))


def file_oper(file, mode, *args):
    # 数据库写入、读取操作
    if mode == "wb":
        with open(file, mode) as f:
            dict = args[0]
            f.write(pickle.dumps(dict))

    if mode == "rb":
        with open(file, mode) as f:
            dict = pickle.loads(f.read())
            return dict


def information(dict, mode, *args):
    """通过匹配mode模式，打印相应的输出信息"""
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, set([])
    if dict:
        for key in dict:
            if mode == "course":
                key.cat_course()
            if mode == "main":
                key.cat_school()
            if mode == "teacher" and key == "teacher":
                dict[key].cat_teacher()
                # dict_info[key] = dict[key]
                set_info.add(dict[key].name)
            if mode == "grade" and key == "grade":
                dict[key].cat_grade()
                set_info.add(dict[key].name)
            if mode == "teacher_center":
                pass
            if type(key) != str:  # key值不是字符串
                dict_info[key.name] = key
    return dict_info, set_info


def school_center():
    # 学校管理中心
    global res_grade
    Flag = True
    while Flag:
        dict_main = file_oper(__db_main, "rb")  # 主字典
        res_dict = information(dict_main, "main")[0]  # 打印学校信息
        school_name = input("\33[34;0m输入要选择的学校名\33[0m：").strip()
        if school_name in res_dict:
            school = res_dict[school_name]  # 匹配选择的学校
            while Flag:
                print("\33[32;1m欢迎进入【%s】学校\33[0m".center(50, "*") % school.name)
                choice = options(list_school)  # 打印当前选项
                if choice == "1":
                    while True:
                        print("\33[32;0m学校【%s】目前已经有的班级信息\33[0m".center(40, "-") % school.name)
                        teacher_dict = file_oper(__db_teacher, "rb")
                        res_course = information(dict_main[school], "None")[0]
                        set_info = set([])
                        if res_course:  # 打印课程与讲师对应关系
                            for i in res_course:
                                k = res_course[i]
                                res_grade = information(dict_main[school][k], "grade", set_info)[1]
                        if_cont = input("\n\33[34;0m是否要创建班级 【y】创建 【b】退出\33[0m:")
                        if if_cont == "y":
                            grade_name = input("\33[34;0m输入要创建班级的名称\33[0m:").strip()
                            course_name = input("\33[34;0m输入要班级要上的课程\33[0m:").strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if dict_main[school][course]:
                                    teacher = dict_main[school][course]["teacher"]
                                    if grade_name not in res_grade:
                                        grade = Grade(grade_name, course_name, teacher.name)
                                        school.create_grade(dict_main, teacher_dict, course, grade, teacher, __db_main,
                                                            __db_teacher)
                                    else:
                                        print("\33[31;0m错误：当前班级已经存在\33[0m")
                                else:
                                    print("\33[31;0m错误：当前课程还没有讲师\33[0m")
                            else:
                                print("\33[31;0m错误:课程【%s】不存在，请先创建课程\33[0m" % course_name)
                        if if_cont == "b":
                            break

                if choice == "2":
                    # 招聘讲师
                    while True:
                        print("\33[32;0m学校【%s】目前已经有的课程与讲师\33[0m".center(40, "-") % school.name)
                        res_course = information(dict_main[school], "None")[0]
                        set_info = set([])
                        if res_course:  # 打印课程与讲师对应关系
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(dict_main[school][k], "teacher", set_info)[1]
                                if not res_teacher:
                                    print("课程【%s】\t讲师【None】" % (i))
                        if_cont = input("\n\33[34;0m是否要招聘讲师 【y】招聘 【b】退出\33[0m:")
                        if if_cont == "y":
                            teacher_name = input("\33[34;0m输入要招聘讲师的名字\33[0m:").strip()
                            teacher_age = input("\33[34;0m输入要招聘讲师的年龄\33[0m:").strip()
                            course_name = input("\33[34;0m输入讲师【%s】要授课的课程\33[0m:" % teacher_name).strip()
                            if course_name in res_course:
                                course = res_course[course_name]  # 创建讲师并写入数据库
                                if teacher_name not in res_teacher:
                                    teacher = Teacher(teacher_name, teacher_age, school.name, course_name)
                                    school.hire_teacher(dict_main, course, teacher, __db_main)
                                else:
                                    print("\33[31;0m错误:教师【%s】已经被聘用\33[0m" % teacher_name)
                            else:
                                print("\33[31;0m错误:课程【%s】不存在，请先创建课程\33[0m" % course_name)
                        if if_cont == "b":
                            break

                if choice == "3":
                    # 创建课程
                    while True:
                        print("\33[32;0m学校【%s】目前已经有的课程\33[0m".center(40, "-") % school.name)
                        res_dict = information(dict_main[school], "course")[0]  # 打印课程信息赋值给字典course_dict
                        if_cont = input("\n\33[34;0m是否要创建课程 【y】创建 【b】退出\33[0m:")
                        if if_cont == "y":
                            course_name = input("\33[34;0m输入要创建的课程\33[0m:").strip()
                            if course_name not in res_dict:  # 课程不存在，创建
                                price = input("\33[34;0m输入课程 【%s】 的价格\33[0m:" % course_name)
                                time = input("\33[34;0m输入课程 【%s】 的周期（月）\33[0m:" % course_name)
                                course = Course(course_name, price, time)  # 创建课程course
                                school.create_course(dict_main, course, __db_main)  # 关联学校和课程
                            else:  # 课程存在
                                print("\33[31;0m错误：当前课程 【%s】 已经存在\33[0m" % course_name)
                        if if_cont == "b":
                            break

                if choice == "4":
                    Flag = False
        if Flag:
            print("\33[31;0m错误：输入的学校 【%s】 不存在\33[0m" % school_name)


def teacher_center():
    # 讲师中心
    print("\33[32;1m欢迎进入讲师中心\33[0m".center(50, "*"))
    teacher_dict = file_oper(__db_teacher, "rb")
    dict_info = information(teacher_dict, "teacher_center")[0]  # 验证登录
    teacher_name = input("\n\33[34;0m输入要登录讲师的名字\33[0m:").strip()
    if teacher_name in dict_info:
        while True:
            print("\33[32;1m欢迎进入讲师【%s】的管理中心\33[0m".center(40, "*") % teacher_name)
            choice = options(list_teacher)
            teacher = dict_info[teacher_name]
            grade = teacher_dict[teacher]["grade"]
            if choice == "1":
                print("\33[32;0m讲师【%s】的班级信息\33[0m".center(40, "-") % teacher.name)
                print("学校【%s】\t课程【%s】\t班级【%s】\t" % (teacher.school, teacher.course, grade.name))
                any = input("\n\33[34;0m输入任意键退出当前\33[0m:")
            if choice == "2":
                print("\33[32;0m讲师【%s】的班级学员列表\33[0m".center(40, "-") % teacher.name)
                print("班级【%s】\n学员【%s】" % (grade.name, grade.student))
                any = input("\n\33[34;0m输入任意键退出当前\33[0m:")
            if choice == "3":
                break
    else:
        print("\33[31;0m错误：讲师【%s】 不存在\33[0m" % (teacher_name))


def student_center():
    # 学员中心
    print("\33[32;1m欢迎进入学员中心中心\33[0m".center(50, "*"))
    while True:
        choice = options(list_student)  # 打印学生中心选项
        if choice == "1":
            student_name = input("\33[34;0m输入学员的名字\33[0m：")
            dict = file_oper(__db_main, "rb")
            teacher_dict = file_oper(__db_teacher, "rb")
            school_dict = information(dict, "main")[0]  # 打印当前可选的学校
            school_name = input("\33[34;0m输入要选择的学校名\33[0m：").strip()
            if school_name in school_dict:
                school = school_dict[school_name]
                if dict[school]:
                    course_dict = information(dict[school], "course")[0]  # 打印当前学校下的课程
                    course_name = input("\33[34;0m输入要选择的课程\33[0m：").strip()
                    if course_name in course_dict:
                        course = course_dict[course_name]
                        if dict[school][course].get("grade"):
                            for i in teacher_dict:
                                if course.name == i.course:
                                    teacher = i
                                    grade = teacher_dict[teacher]["grade"]
                            print("课程【%s】的费用为【%s】" % (course.name, course.price))
                            if_pay = input("\33[34;0m是否支付当前费用 支付【y】\33[0m:")
                            if if_pay == "y":  # 上面全部匹配成功，选课成功
                                grade.add_student(student_name, teacher_dict, teacher, __db_teacher)
                                print("\33[31;0m选课成功\33[0m")
                                any = input("\n\33[34;0m输入任意键退出当前\33[0m:")
                        else:
                            print("\33[31;0m错误：课程没有班级\33[0m")
                    else:
                        print("\33[31;0m错误：课程不存在\33[0m")
                else:
                    print("\33[31;0m错误：当前学校没有课程\33[0m")
        if choice == "2":
            break


def options(list):
    # 打印可选择的操作模式，并返回选择值
    for i, v in enumerate(list):
        print(i + 1, v)
    choice = input("\33[34;0m选择要进入模式\33[0m:")
    return choice


def start():
    '''程序开始'''
    while True:
        print("\33[35;1m欢迎进入选课系统\33[0m".center(50, "#"))
        choice = options(list_main)  # 打印选项
        if choice == "1":
            student_center()  # 学生中心
        if choice == "2":
            teacher_center()  # 教师中心
        if choice == "3":
            school_center()  # 学校中心
        if choice == "4":
            break


def init_database():
    '''数据库初始化，不存在则创建，存在跳过'''
    bj = School("北京", "北京市")
    sh = School("上海", "上海市")
    if not os.path.exists(__db_teacher):
        dict = {bj: {}, sh: {}}
        file_oper(__db_main, "wb", dict)
    if not os.path.exists(__db_teacher):
        dict = {}
        file_oper(__db_teacher, "wb", dict)


if __name__ == '__main__':
    init_database()  # 初始化数据库
    list_main = ["学生中心", "讲师中心", "学校中心", "退出"]
    list_school = ["创建班级", "招聘讲师", "创建课程", "返回"]
    list_teacher = ["查看班级", "查看班级学员列表", "返回"]
    list_student = ["学员注册", "返回"]
    start()
