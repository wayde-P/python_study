import hashlib

m = hashlib.md5()
m.update(b"hello")
m.update("hlo")
print(m.digest())