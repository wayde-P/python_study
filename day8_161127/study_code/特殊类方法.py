class com(object):
    '''
    w我擦擦擦擦啊c
    是是是是是是
    '''
    def func(self,name):
        print("%s is func",name)
        pass
    def __str__(self):
        return "wocalei"

print(com.__doc__)

print(com.__module__)
a = com()
# 　　__module__ 表示当前操作的对象在那个模块
print(a.__class__)
# 　　__class__     表示当前操作的对象的类是什么

print(a.__dict__)
#__dict__ 查看类或对象中的所有成员
print(a)

