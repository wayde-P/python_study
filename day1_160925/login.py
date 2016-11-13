import os

flag = False
for i in range(3):
    if flag:
        break
    valid_name = input("Input you name:")
    valid_password = input("Input you password")
    password_file = open("E:\python\OneDrive\zewei\python\py_s15\day1_160925\password", 'r')
    for line in password_file:
        valid_name_password = valid_name + ':' + valid_password  # 拼用户名和密码的字符串用于比对
        print(valid_name_password)
        if valid_name_password in line:  # 在文件里找匹配的字符串
            print("welcome login this system!")
            flag = True
            break
        print("wrong user or password")
    #            password_file.close()
    #       else:
    #      print("wrong user or password")
else:
    print("this like attck. user will be lock ")
    password_file_tmp = open("E:\python\OneDrive\zewei\python\py_s15\day1_160925\password.tmp", 'a')
    for line in password_file:
        if valid_name_password in line:  # 在文件里找匹配的字符串
            line = line.replace(line, 'lock:valid_name_password')
        password_file_tmp.write(line)
    password_file_tmp.close()
    #       os.rename("E:\python\OneDrive\zewei\python\py_s15\day1_160925\password.tmp",\
    #                 "E:\python\OneDrive\zewei\python\py_s15\day1_160925\password")
