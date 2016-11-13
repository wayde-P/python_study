user_status = False


def login(func):
    def inner(arg1):
        _username = "zhang"
        _password = "zhang"
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pass:")

        if _username == username and _password == password:
            print("welcom login")
            user_status = True

        if user_status == True:
            func(arg1)
    return inner


def home():
    print("----main page------")


def ameriac():
    print("welcome to america")


@login
def japan(b):
    print("welcome to japan")
    print(b)


def shandong():
    print("welcome to shandong")


home()
#ameriac()
japan(11)
