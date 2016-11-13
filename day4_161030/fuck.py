def stu_register(name, age, *args):  # *args 会把多传入的参数变成一个元组形式
    print(name, age, args)
    tu = args
    print(type(tu))
    print(tu[0])

#
# stu_register("Alex", 22)
# # 输出
# # Alex 22 () #后面这个()就是args,只是因为没传值,所以为空

stu_register("Jack", 32, "CN", "Python")
# 输出
# Jack 32 ('CN', 'Python')