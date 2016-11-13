import json

data = {
    "name":"wayde",
    "age":12,
    "sex":"M",
}
# f = open("ww","w",encoding='utf-8')
# json.dump(data,f)
f = open("ww","r",encoding='utf-8')
print(json.load(f)["sex"])
