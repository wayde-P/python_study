import random

def gen_person(n):
    ids=list(range(1,n+1))
    yi = ["候","赵","菜","糕","力",]
    er = ["立","亮","成","育","达",]
    san = ["春","平","功","良","康",]
    for i in range(n):
        id = ids[i]
        age =   random.randint(18,69)
        name = random.choice(yi)+random.choice(er)+random.choice(san)b
        print(id,age,name)

gen_person(20)