import re

cal = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

strip_space = re.sub(r' +', '', cal)  # 去掉无用的空格
print(strip_space)
a = re.search(r'\([^()]+\)', strip_space).group()  #找出最里层的括号

no_kuohao = re.search(r'[^()]+', a).group()  #去掉括号

li_a = re.sub(r'\/', ' ', no_kuohao).split(" ")  # 序列化
result = eval("%s / %s" % (li_a[0], li_a[1]))  #计算
print(result)
