from django.shortcuts import render
from  bbs import models


# Create your views here.


def index(request):
    categories = models.Category.objects.filter(set_as_top_menu=True)
    return render(request, 'index.html', {"categories": categories})


def category(request, category_id):
    categories = models.Category.objects.filter(set_as_top_menu=True)

    articles = models.Article.objects.filter(category_id=category_id)

    return render(request, 'index.html', {"categories": categories, "articles": articles})
