names = ["tom", "jerry", "shuke", "beita", ""]
names.insert(2, "bbb")  # 插入到index的前面

# 删除
names.remove("bbb")
del names[3]
names.pop()  # 删除并返回删除的值
# 改
names[1] = '汤姆'
# 查
names[1]
names[-3:]  # 获取最后3个元素

names.index()  # 取下标
names.extend()  # 合并字符串
