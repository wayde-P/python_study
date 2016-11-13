import os

notic = '''1.查询
2.添加
3.删除'''

while True:
    print('请输入你要选择的操作:'.center(30, '#'))
    print(notic)
    print('END'.center(40, '#'))
    choice = int(input(">>:"))
    if choice > 3:
        print("超出范围,重新选择")
        continue
    elif choice == 1:
        with open('haproxy.txt', 'r', encoding='utf-8') as ha:
            for i in ha:
                if i.strip().startswith("backend"):
                    FQDN = i.split()[1]
                    dic_backend = {FQDN: []}  # backend 名字加入字典
                elif i.strip().startswith("server"):
                    dic_backend[FQDN].append(i.strip().split())
        for f in dic_backend.keys():
            print("当前存在的backend:",f)
        choice_fqdn = input("请输入要查询的域名:").strip()
        if choice_fqdn in dic_backend:  # print(dic_backend[choice])
            for k in enumerate(dic_backend[choice_fqdn], 1):
                print(k[0], ".", *k[1])
        else:
            print("你输入的不存在,请重新输入")
    elif choice == 2 or choice == 3:
        backend = input("backend: ").strip()
        server = input("server: ").strip()
        weight = input("weight: ").strip()
        maxconn = input("maxconn: ").strip()
        new_backend_server = "        server {a} {a} weight {b} maxconn {c}\n".format(a=server, b=weight, c=maxconn)
        if choice == 2:
            with open('haproxy.txt', 'r', encoding='utf-8') as ha, open('haproxy_new', 'w+',
                                                                        encoding='utf-8') as ha_new:
                for i in ha:
                    # record_num = 1
                    if i.strip().startswith("backend") and i.split()[1] == backend:
                        ha_new.write(i)
                        # server_info = new_backend_server
                        ha_new.write(new_backend_server)
                    else:
                        ha_new.write(i)
            os.remove("haproxy.txt")
            os.rename("haproxy_new", "haproxy.txt")
            exit()
        elif choice == 3:
            with open('haproxy.txt', 'r', encoding='utf-8') as ha, \
                    open('haproxy_new', 'w+', encoding='utf-8') as ha_new:
                current_backend = ''
                for i in ha:
                    if i.strip().startswith("backend") and i.split()[1] == backend:
                        current_backend = 'yes'
                    if (current_backend == 'yes') and \
                            (i.strip().startswith("server")) and \
                            (i.strip() == new_backend_server.strip()):
                        current_backend = 'no'
                        continue
                    else:
                        ha_new.write(i)
            os.remove("haproxy.txt")
            os.rename("haproxy_new", "haproxy.txt")
            exit()

