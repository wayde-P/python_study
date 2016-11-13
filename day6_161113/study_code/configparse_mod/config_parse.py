import configparser

a= configparser.ConfigParser()
print(a.sections())
print(a.read("conf.ini"))
print(a.sections())
