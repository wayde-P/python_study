import re


# print(result)
def plus(li_a):
    num_1 = float(li_a[0])
    num_2 = float(li_a[1])
    # return ("+",num_1 + num_2)
    return num_1 + num_2


def minus(li_a):
    num_1 = float(li_a[0])
    num_2 = float(li_a[1])
    return num_1 - num_2


def multiply(li_a):
    num_1 = float(li_a[0])
    num_2 = float(li_a[1])
    if '-' in li_a[0] and '-' in li_a[1]:
        return "+%s" % (num_1 * num_2)
    else:
        return num_1 * num_2


def divide(li_a):
    num_1 = float(li_a[0])
    num_2 = float(li_a[1])
    return num_1 / num_2


def Operation(no_kuohao):
    opt_dic = {
        '+': plus,
        '-': minus,
        '*': multiply,
        '/': divide
    }
    opt = re.findall(r'[\+\*\/]', no_kuohao)  # 找出运算符
    # print("opt", opt)
    li_num = re.sub(r'[\+\*\/]', ' ', no_kuohao).split(" ")  # 替换掉运算符,把数字存进列表
    # print("li_num", li_num)
    if len(li_num) == 1:  # 此处判断减法的几种情况
        if re.search(r'--', no_kuohao):  # 正/负数减负数
            opt = ['+']  # 减负数实际上就是做加法
            li_num = li_num[0].replace('--', ' ').split(" ")  # 把后面的负数替换成正数
            # print(li_num[0].replace('--',' ').split(" "))
            # print(li_num) #
        elif re.match(r'\d', no_kuohao):  # 正数减正数
            opt = ['-']
            li_num = li_num[0].split('-')
        elif re.match(r'-', no_kuohao):  # 负数减正数
            opt = ['-']
            tmp_li_num = no_kuohao.split("-")[1:]
            li_num = ["-%s" % tmp_li_num[0], tmp_li_num[1]]
            # print(no_kuohao.split("-"))
            # print(li_num)

    return opt_dic[opt[0]](li_num)
    # result = eval(li_a[0])
    # return str(result)


def chengchu(cheng_chu):
    # cheng_chu = re.search(r'[^()]+', cheng_chu).group()
    # if re.search(r'(-?\d+(\.\d+)?)[\*\/](-?\d+(\.?\d+)?)', cheng_chu).group():
    if re.findall(r'[\*\/]', cheng_chu):
        while True:
            # small_expression = re.search(r'(\d+(\.\d+)?)[\*\/](-?\d+(\.?\d+)?)', cheng_chu).group() #找到一个乘法或除法的式子
            small_expression = re.search(r'(-?\d+(\.\d+)?)[\*\/](-?\d+(\.?\d+)?)', cheng_chu).group()  # 找到一个乘法或除法的式子
            result = Operation(small_expression)  # 得出结果
            cheng_chu = cheng_chu.replace(small_expression, str(result))  # 替换回原来的式子
            # print(small_expression)
            # print(result)
            # print(cheng_chu)
            # print(re.sub(r'[\*\/]', ' ', cheng_chu).split(' '))
            if len(re.sub(r'[\*\/]', ' ', cheng_chu).split(' ')) == 1:
                break
    return cheng_chu


def jiajian(jia_jian):
    # if re.search(r'(-?\d+(\.\d+)?)[\+\-](-?\d+(\.?\d+)?)', jia_jian).group():
    if jia_jian.startswith('-') and not re.findall(r'[\+\-]', jia_jian.lstrip('-')):
        return jia_jian
    elif re.findall(r'[\+\-]', jia_jian):
        while True:
            # if len(re.sub(r'[\+\-]', ' ', jia_jian.lstrip('-')).split(' ')) == 1:
            if len(re.findall(r'(-?\d+(\.\d+)?)[\+\-](-?\d+(\.?\d+)?)', jia_jian)) == 0:
                break
            # small_expression = re.search(r'(\d+(\.\d+)?)[\+\-](-?\d+(\.?\d+)?)', jia_jian).group()
            small_expression = re.search(r'(-?\d+(\.\d+)?)[\+\-](-?\d+(\.?\d+)?)', jia_jian).group()
            # print(small_expression)
            result = Operation(small_expression)
            # print(result)
            jia_jian = jia_jian.replace(small_expression, str(result))
            # print(cheng_chu)
            # print(re.sub(r'[\*\/]', ' ', cheng_chu).split(' '))
    return jia_jian
cal = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#cal = "1-9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14"
print("请输入计算公式:如:", cal)
while True:
    cal = input(">>(quit): ").strip()
    cut_space = re.sub(r' +', '', cal)  # 去掉无用的空格
    if 'quit' == cal:
        exit("bye bye !")
    elif len(re.findall(r'[\+\-\*\/]', cal.lstrip('-'))) == 0:
        print(cal)
    elif len("".join(re.findall(r'[\(\)]+', cal.lstrip('-')))) % 2 != 0:
        # print(re.findall(r'[\(\)]+', cal.lstrip('-')))
        # print(len("".join(re.findall(r'[\(\)]+', cal.lstrip('-')))))
        print("括号数量不对,请检查")
    elif 0 < len(re.findall(r'[\(\)]+', cal.lstrip('-'))) and \
                            len("".join(re.findall(r'[\(\)]+', cal.lstrip('-')))) % 2 == 0:
        while True:
            # print("to back")
            if re.findall(r'[()]', cut_space):
                find_deep_parentheses = re.search(r'\([^()]+\)', cut_space).group()  # 找出最里层的括号
                cut_parentheses = re.search(r'[^()]+', find_deep_parentheses).group()  # 去掉括号
                result = jiajian(chengchu(cut_parentheses))                     #调用函数计算结果
                cut_space = cut_space.replace(find_deep_parentheses, result)  # 把计算结果替换到原算式
                # print("===========>", cut_parentheses, result)
                print("-->", find_deep_parentheses, result)
                print('##>', cut_space)
            else:
                print("结果:", jiajian(chengchu(cut_space)))
                break
    else:
        print("结果:", jiajian(chengchu(cut_space)))
