# boy_age=39
# for i in range(3):
#     guess_age=int(input("input age:"))
#     if guess_age == boy_age:
#         print("yes , niubi")
#         break
#     elif guess_age > boy_age :
#         print("try smaller")
#     else:
#         print("try biger")

for i in range(8):
    # print(i)
    if i < 4:
        continue
    else:
        print(i)
else:
    print("顺利结束")