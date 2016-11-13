oldboy_age = 39
guess_age = int(input("inpu guess age:"))

print( type(guess_age) )
if guess_age == oldboy_age :
    print ("correct")
elif guess_age > oldboy_age:
    print ("try smaller..")
else:
    print ("try bigger")

