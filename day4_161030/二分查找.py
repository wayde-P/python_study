data = range(0, 50, 2)


def two(li, find_num):
    middle_pbs = len(li) / 2
    if li[middle_pbs] == find_num:
        print('找到了')
    elif li[middle_pbs] < find_num:
        print("去右边", li[middle_pbs])
        return two(li[0:middle_pbs], find_num)
    elif li[middle_pbs] > find_num:
        print("去左边", li[middle_pbs])
        return two(li[middle_pbs:], find_num)

two(data,12)