from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    # obj = request.FILES.get('upload')
    # print(obj.name)
    # f = open(obj.name, 'wb')
    # for line in obj.chunks():
    #     f.write(line)
    # f.close()
    return HttpResponse('OK')
