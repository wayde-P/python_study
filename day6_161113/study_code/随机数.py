import random
import string
print(random.random())
print(random.randint(1,9))
print(random.randrange(1,9))

str_li = string.ascii_letters + string.digits
print("".join(random.sample(str_li,8)))
# print(str_li)
