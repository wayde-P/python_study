import os
import sys

ATM_core = "%s/ATM"% os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ATM_core)
sys.path.append(ATM_core)

from core import transaction
from core import auth


shopping_car = {}
shop_list = [
    ['iphone', 1000],
    ['bike', 1500],
    ['mac_book', 8000],
    ['衣服', 500],
    ['咖啡', 300],
    ['mac_mini', 5000]
]
pay=0

# while True:
#     salary = input("请输入你的工资:")
#     if salary.isdigit():
#         salary = int(salary)
#         break
#     else:
#         print("请输入正确的工资!")
@auth.login
def xiaofei(user):
    global pay
    transaction.make_transaction("consume",user,pay)

while True:
    print("shopping list".center(30, "-"))
    for i, ele in enumerate(shop_list):
        print(i + 1, ele[0], ele[1])
    print("end".center(30, "-"))
    product = input("请选择商品序号[quit]:")
    if product.isdigit():  # 判断是否为数字
        product = int(product)  # 转换为int
        if (product > 0) and (len(shop_list) + 1 > product):  # 判断输入的数字是否正确

                # salary -= shop_list[product - 1][1]
                pay = pay + shop_list[product - 1][1]
                if shop_list[product - 1][0] in shopping_car:  # 添加商品至购物车
                    shopping_car[shop_list[product - 1][0]] += 1
                else:
                    shopping_car[shop_list[product - 1][0]] = 1
                # print("你添加了[%s] 到购物车,你的余额还有%s" % (shop_list[product - 1][0], salary))

        else:
            print("没有此商品...")
    elif product == 'quit':
        print("已购买的商品为".center(40, '#'))
        for key in shopping_car.keys():
            print("%s * %s".center(40,' ')%(key,shopping_car[key]))
        print("总计消费: %s".center(40,' ')%pay)
        xiaofei()

        exit()
    else:
        continue
