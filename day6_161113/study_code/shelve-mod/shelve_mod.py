import shelve

d = shelve.open("shelve-test")

def sayhello(name):
    print("say hai ",name)

lia = [1, 2 ,23]
dica= {"a":22,"bb":33}

d["d_sayhello"] = sayhello
d["lia"] = lia
d["dica"] = dica

