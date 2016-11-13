count=0
boy_age=22
while count < 3 :
    guess_age=input("age>>>")
    if guess_age.isdigit():
        guess_age = int(guess_age)
    else:
        continue
    if guess_age == boy_age:
        print("ok")
        break
    elif guess_age > boy_age :
        print("to big")
    else:
        print("to small")
    count +=1
