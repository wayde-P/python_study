username = input("Input Username: ")
#判断用户名是否被锁定
lock_file = open("lockfile", 'r')
all_lock_file = lock_file.read()
if username in all_lock_file:
    print("This user is lock ....")
    lock_file.close()
    exit()

#判断密码是否正确
user_file = open("password",'r')
all_user_file=user_file.read()
for i in range(3):
    password = input("Input Password: ")
    valid_name_password = username + ':' + password #拼凑用户名和密码的字符串
    if valid_name_password in all_user_file:    #使用上面拼凑的字符串查找
        print("Welcome login system!!!")
        break
else:
    #锁定用户名
    lock_file = open("lockfile", 'a')
    lock_file.write(username + '\n')
    lock_file.close()
    print("like attack . username will be lock")
