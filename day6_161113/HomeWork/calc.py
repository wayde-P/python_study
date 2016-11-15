import re

cal = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

strip_space = re.sub(r' +', '', cal)  # 去掉无用的空格
# print(strip_space)
a = re.search(r'\([^()]+\)', strip_space).group()  #找出最里层的括号

no_kuohao = re.search(r'[^()]+', a).group()  #去掉括号
# print(re.findall(r'[\+\*\/]',no_kuohao))

# li_a = re.sub(r'\/', ' ', no_kuohao).split(" ")  # 序列化
# result = -28  # 计算


# print(result)


def Operation(no_kuohao):
    opt = re.findall(r'[\+\*\/]', no_kuohao)

    li_a = re.sub(r'[\+\*\/]', ' ', no_kuohao).split(" ")
    if len(li_a) != 1:
        # opt = li_a[1]
        # print(li_a)
        if len(opt) == 0:
            opt = '-'
        # print(opt)
        print(opt)
        num_1 = li_a[0]
        num_2 = li_a[1]
        print("%s%s%s" % (num_1, opt[0], num_2))
        result = eval("%s%s%s" % (num_1, opt[0], num_2))

        return str(result)
    else:
        result = eval(li_a[0])
        return str(result)


strip_space = strip_space.replace(a, Operation(no_kuohao))
print(strip_space)
# print(re.search(r'\([^()]+\)', strip_space).group())
b = re.search(r'\([^()]+\)', strip_space).group()


# print(re.search(r'-?\d[\*\/]-?\d', b).group())


def chengchu(cheng_chu):
    while True:
        small_expression = re.search(r'(-?\d+\.?\d+)[\*\/](-?\d+\.?\d+)', cheng_chu).group()
        print(small_expression)
        result = Operation(small_expression)
        print(result)
        cheng_chu = cheng_chu.replace(small_expression, result)
        print(cheng_chu)
        if len(re.sub(r'[\*\/]', ' ', no_kuohao).split(' ')) == 1:
            break
    return no_kuohao


print(chengchu(b))





# 匹配减号 -?\d-{1,2}\d
# 匹配乘除 -?\d[\*\/]-?\d
# 9-2*50/5 9-20 -11
#
