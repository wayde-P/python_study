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
def plus(li_a):
    num_1 = int(li_a[0])
    num_2 = int(li_a[1])
    return num_1 + num_2


def minus(li_a):
    num_1 = int(li_a[0])
    num_2 = int(li_a[1])
    return num_1 - num_2


def multiply(li_a):
    num_1 = int(li_a[0])
    num_2 = int(li_a[1])
    return num_1 * num_2


def divide(li_a):
    num_1 = int(li_a[0])
    num_2 = int(li_a[1])
    return num_1 / num_2




def Operation(no_kuohao):
    opt_dic = {
        '+': plus,
        '-': minus,
        '*': multiply,
        '/': divide
    }
    opt = re.findall(r'[\+\*\/]', no_kuohao)  # 找出运算符
    print("opt", opt)
    li_num = re.sub(r'[\+\*\/]', ' ', no_kuohao).split(" ")  # 替换掉运算符,把数字存进列表
    print("li_num", li_num)
    if len(li_num) == 1:
        if len(opt) == 0:  # 此处判断减负数
            opt = ['+']  # 减负数实际上就是做加法
            li_num = li_num[0].replace('--', ' ').split(" ")  # 把后面的负数替换成正数
            # print(li_num[0].replace('--',' ').split(" "))
            # print(li_num)

    print(opt_dic[opt[0]](li_num))
    # result = eval(li_a[0])
    # return str(result)


Operation('-1-2')

strip_space = strip_space.replace(a, Operation(no_kuohao))
print(strip_space)
b = re.search(r'\([^()]+\)', strip_space).group()
print(b)


def chengchu(cheng_chu):
    cheng_chu = re.search(r'[^()]+', cheng_chu).group()
    while True:
        small_expression = re.search(r'(-?\d+(\.\d+)?)[\*\/](-?\d+(\.?\d+)?)', cheng_chu).group()
        # print(small_expression)
        result = Operation(small_expression)
        # print(result)
        cheng_chu = cheng_chu.replace(small_expression, result)
        # print(cheng_chu)
        # print(re.sub(r'[\*\/]', ' ', cheng_chu).split(' '))
        if len(re.sub(r'[\*\/]', ' ', cheng_chu).split(' ')) == 1:
            break
    return cheng_chu


def jiajian(jia_jian):
    while True:
        small_expression = re.search(r'(-?\d+(\.\d+)?)[\+\-](-?\d+(\.?\d+)?)', jia_jian).group()
        # print(small_expression)
        result = Operation(small_expression)
        # print(result)
        jia_jian = jia_jian.replace(small_expression, result)
        # print(cheng_chu)
        # print(re.sub(r'[\*\/]', ' ', cheng_chu).split(' '))
        if len(re.sub(r'[\+\-]', ' ', jia_jian).split(' ')) == 1:
            break
    return jia_jian


c = chengchu(b)
print(c)
print(jiajian(c))





# 匹配减号 -?\d-{1,2}\d
# 匹配乘除 -?\d[\*\/]-?\d
# 9-2*50/5 9-20 -11
#
