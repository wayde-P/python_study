# name = input("name:")
# age = input("age:")
# job = input("job:")
# hobby = input("hobby:")
#
# info='''
# ---------info of %s -------
# name : %s
# age  : %s
# job  : %s
# hobby: %s
# ------------end------------
# ''' %(name,name,age,job,hobby)
#
# print(info)

# a = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4]
a = [
    ['iphone', 1000],
    ['bike', 1500],
    ['mac_book', 8000],
    ['mac_book', 8000],
    ['衣服', 500],
    ['mac_book', 8000],
    ['bike', 1500],
    ['iphone', 1000],
    ['mac_book', 8000],
    ['衣服', 500],
    ['咖啡', 300]
]

aa = dict(iphone=21000, bike=1500, 衣服=400, macbook=12800, 咖啡=333)
# li=[]
# for i,o in a:
#     li.append(i)
# else:
#     li=set(li)
for aac in aa:
    print(aac)
# s_b = set(a)  # sort and unis
# for i in s_b:
#     print("item", i, "*", a.count(i))
#     # print(a.count(i))
