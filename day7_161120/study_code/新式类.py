class A:
    def __init__(self):
        print('This is A')

    def save(self):
        print('save method from A')


class B(A):
    def __init__(self):
        print('This is B')


class C(A):
    def __init__(self):
        print('This is C')

    def save(self):
        print('save method from C')


class D(C, B):
    def __init__(self):
        print('This is D.')


e = D()
e.save()
