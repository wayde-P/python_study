import os

column_id = dict(staff_id=0, group=1, name=2, age=3, phone=4, dept=5, enroll_date=6)


def info_list():
    data = []
    with open("user_new", 'r', encoding='utf-8') as r_file:
        for line in r_file:
            data.append(line.strip().split(","))
        return data


def select(column='*', condition="1"):
    column_count = 0
    b = []
    for i in info_list():
        staff_id = int(i[0])
        group = int(i[1])
        name = i[2]
        age = int(i[3])
        phone = int(i[4])
        dept = i[5]
        enroll_date = i[6]
        if column != '*':
            r_li = []  # 初始化return列表
            for j in column.split(','):
                if eval(condition.replace('=', '==')):
                    if j == column.split(',')[-1]:
                        r_li.append(i[column_id[j]])
                        b.append(r_li)  # 添加数据到列表
                        column_count += 1  # 计数器加1
                        r_li = []  # 置空,为下一次加数据
                    else:
                        r_li.append(i[column_id[j]])  # 添加数据到列表
        elif column == '*' and eval(condition.replace('=', '==')):
            b.append(i)
            column_count += 1
    b.append(column_count)
    return b


def select_like(lie='*', con_di="1", key="1"):
    b = []
    r_li = []
    column_count = 0
    for i in select(column='*', condition="1")[0:-1]:
        if i[column_id[con_di]].startswith(key):
            if lie == '*':
                b.append(i)
                column_count += 1
            else:
                for j in lie.split(','):
                    if j == lie.split(',')[-1]:
                        r_li.append(i[column_id[j]])
                        b.append(r_li)  # 添加数据到列表
                        column_count += 1  # 计数器加1
                        r_li = []  # 置空,为下一次加数据
                    else:
                        r_li.append(i[column_id[j]])
    b.append(column_count)
    return b


def insert(i_data):
    data = i_data.split(",")
    group = data[0]
    Name = data[1]
    age = data[2]
    Phone = data[3]
    Dept = data[4]
    Enroall_data = data[5]
    all_phone = select(column="phone")
    auto_jia = select(column="staff_id")

    with open('user_new', "a+", encoding='utf-8') as w_file:
        for ph in all_phone[0:-1]:
            if Phone == ph[0]:
                info = "This phone an in table ! please check !"
                break
        else:
            n_data = "\n%s,%s,%s,%s,%s,%s,%s" % (int(auto_jia[-2][0]) + 1, group, Name, age, Phone, Dept, Enroall_data)
            w_file.write(n_data)
            info = "新增了此条记录: %s" % n_data
        return info


def delete(number):
    with open('user_new', 'r', encoding='utf-8') as r_file, \
            open('user_write', "w+", encoding='utf-8') as w_file:
        print(select(condition="staff_id = %s" % number, column="*")[0])
        if len(select(condition="staff_id = %s" % number, column="*")[0]) != 0:
            search_data = ",".join(select(condition="staff_id = %s" % number, column="*")[0])
        else:
            return "无此条记录！"
        for i in r_file:
            if i.strip() == search_data:
                continue
            else:
                w_file.write(i)
    os.remove("user_new")
    os.rename("user_write", "user_new")
    return "[%s]记录被删除" % search_data


def update(old, new):
    count = 0
    with open('user_write', "w+", encoding='utf-8') as w_file:
        for i in info_list():
            if old in i:
                idx = i.index(old)
                i[idx] = new
                count += 1
                w_data = ",".join(i)
                w_file.write(w_data)
        return "此次更新了 %s 条记录" % count


def p_info(data):
    for i in data[0:-1]:
        print("\t".join(i))
    print("共有 %s 条记录被匹配" % data[-1])
    return True

msg = '''
请按照以下格式输入:
    SELECT * FROM staff_table
    SELECT name,age FROM staff_table WHERE age > 22
    SELECT * FROM staff_table WHERE enroll_date LIKE "2013"
    INSERT INTO staff_table (group,name,age,phone,dept,enroll_date) VALUES(1,张三,33,18989898989,IT,2017-06-05)
    UPDATE staff_table SET dept = Market WHERE where dept = IT
    DELETE [staff_id]
'''
print(msg)
while True:
    user_input = str(input("退出:q >>:"))
    input_list = user_input.strip().split(" ")
    first_opt = input_list[0].lower()
    if user_input == 'q':
        exit()
    elif len(user_input) == 0:
        continue
    if first_opt == "select" and len(input_list) == 8:
        if input_list[6].lower() == 'like':
            p_info(select_like(lie="%s" % (input_list[1]), con_di="%s" % (input_list[5]),
                               key="%s" % (input_list[-1].strip("\""))))
        else:
            p_info(select(condition="%s" % input_list[-3:], column="%s" % (input_list[1])))
    elif first_opt == "select" and len(input_list) == 4:
        p_info(select(column="%s" % (input_list[1])))
    elif first_opt == "insert" and (len(input_list)) == 5:
        input_list[-1].lower().rstrip("VALUES(").rstrip(")")
        print(insert(input_list[-1].lstrip("VALUES(").rstrip(")")))
    elif first_opt == "update" and len(input_list) == 11:
        print(update(new='%s' % (input_list[5].strip("\"")),
                     old='%s' % (input_list[-1].strip("\""))))
    elif first_opt == "delete" and len(input_list) == 2:
        delete(number=input_list[1])
    else:
        continue
