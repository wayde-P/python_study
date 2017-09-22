from django.shortcuts import render
from django.shortcuts import HttpResponse

import json
# Create your views here.

def authority_load(request):
    # if request == "GET":
    with open("/Users/zewei/PycharmProjects/check_authority/authority_monitor/normal.json", "r") as file:
        normal_txt=file.readline()
    with open("/Users/zewei/PycharmProjects/check_authority/authority_monitor/wrong.json", "r") as file:
        wrong_txt=file.readline()
    normal_dict=json.loads(normal_txt)
    wrong_dict=json.loads(wrong_txt)
    # all_dict="hello"
    # print(type(all_dict))
    return render(request,"index.html",{"normal_dict":normal_dict,"wrong_dict":wrong_dict})
    # return render(request,"index.html",{all_dict:json.dumps(all_dict)})

def test(request):
    return render(request,"test.html")