import hashlib

m = hashlib.md5()
m.update(b"hello")
m.update(b"hlo")
print(m.digest())