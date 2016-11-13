msg = 'hello world'
print(msg.capitalize())  # 开头大写
print(msg.center(20, '#'))  # 居中显示
print(msg.count('l'))
print(msg.endswith('l'))  # 判断字符串的结尾字符
msg1 = 'a\tb'
# format的三种使用方式
print('{name} {hobby} {age}'.format(name='alze', age='bb', hobby='zz'))
print('{} {} {}'.format('alze', 'bb', 'zz'))
print('{0} {1} {0} {2}'.format('zzz', 'ddd', 'aaa'))
msg2='33'
print(msg.isalnum())#判断是否是字母或者是数字的组合
print(msg.isalpha())#判断是否是字母的组合
print(msg.isdecimal())#判断是否是十进制
print(msg.isnumeric())#判断是否是Unicode数字
print(msg.strip())#去掉空格
print(msg.isdigit())


