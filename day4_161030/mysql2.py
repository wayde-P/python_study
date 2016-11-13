c_id = {
    "staff_id": 0,
    "group": 1,
    "name": 2,
    "age": 3,
    "phone": 4,
    "dept": 5,
    "enroll_date": 6}


# def select(lie, biao, T_lie, Tiaojian ):
# 返回字典
def info_list():
    # data = []
    # with open("user_new", 'r', encoding='utf-8') as file:
    #     for line in file:
    #         data.append(line.strip().split(","))
    #     return data
    stu_info = {}
    with open("user_new", "r", encoding='utf-8') as r_file, \
            open("user_new_dict", "w+", encoding='utf-8') as w_file:
        for i in r_file:
            li_i = i.strip().split(',')
            stu_info[li_i[4]] = {'staff_id': li_i[0],
                                 'group': li_i[1],
                                 'name': li_i[2],
                                 'age': li_i[3],
                                 'phone': li_i[4],
                                 'dept': li_i[5],
                                 'enroll_date': li_i[6]}
        return stu_info


def select(condition='',column='*'):  # condition 条件
    if column != '*':
        # for column_title in column.split(','):
        #     print(column_title, "\t", end='')
        # print("")
        # for i in info_list():
        #     for c in column.split(','):
        #         if c == column.split(',')[-1]:
        #             print(i[c_id[c]])
        #         else:
        #             print(i[c_id[c]], "\t", end="")
        data = []
        # print(info_list())
        for i in info_list().keys():
            # print(info_list()[i])
            newli=[]
            for j in column.strip().split(','):
                # print(j)
                # if info_list()[i][j]:
                    newli.append(info_list()[i][j])
                # print()
            data.append(newli)
        print(data)


# def where(data=''):
#     for i in select(data.strip().split()[0]):
#         pass


select(condition="age > 22",column='group,name,age,phone')
# where("age > 22")
