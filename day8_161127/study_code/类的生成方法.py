def func(self):
    print("hello woca")


Foo = type('Foo', (object,), {"func": func})
a = Foo()
a.func()
