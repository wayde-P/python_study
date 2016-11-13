data = [1, 2, 3, 4, 5]

# 列表生成器
data = [i * 2 if i > 3 else i for i in data]

data = []
for i in data:
    data.append(i * 2 if i > 3 else i)

print(data)


def fib(num):
    a, b = 0, 1
    
