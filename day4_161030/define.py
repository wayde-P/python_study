# def sayhi():
#     print("hello. I'm siri!")
#
#
# sayhi()
#
#
# def stu_register(name, age, country="CN", course='数学'):
#     print('''--注册信息--
#     姓名:%s
#     age:%s
#     国籍:%s
#     课程:%s
#     其他:
#     ''')%(name,age,country,course)
#
#
# stu_register("张珊", 18)
# stu_register("李斯", 19, country="jp")
# stu_register("王武", 20, course='英语')
#
#
# a = 11
#
#
# def change_a():
#     global a
#     a = 22
#     # print(a)
# change_a()
# print(a)

def calc(n):
    if n//2 > 0:
        calc(n//2)
    print(n)
calc(20)