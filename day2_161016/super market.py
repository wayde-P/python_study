shopping_car = []
shop_list = [
    ['iphone', 1000],
    ['bike', 1500],
    ['mac_book', 8000],
    ['衣服', 500],
    ['咖啡', 300],
    ['mac_mini', 5000]
]

while True:
    salary = input("请输入你的工资:")
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print("请输入正确的工资!")
while True:
    print("shopping list".center(30, "-"))
    for i, ele in enumerate(shop_list):
        print(i + 1, ele[0], ele[1])
    print("end".center(30, "-"))
    product = input("请选择商品序号[quit]:")
    if product.isdigit():  # 判断是否为数字
        product = int(product)  # 转换为int
        if (product > 0) and (len(shop_list) + 1 > product):  # 判断输入的数字是否正确
            if shop_list[product - 1][1] < salary:
                salary -= shop_list[product - 1][1]
                shopping_car.append(shop_list[product - 1])  # 添加商品至购物车
                print("你添加了[%s] 到购物车,你的余额还有%s" % (shop_list[product - 1][0], salary))
            else:
                print("你的余额不够.你只有%s" % salary)
        else:
            print("没有此商品...")
    elif product == 'quit':
        print("已购买的商品为".center(40, '#'))
        # print(p, "\t".format(), o)
        print("你的余额还剩下", salary)
        exit()
    else:
        continue
