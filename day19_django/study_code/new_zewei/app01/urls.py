"""new_zewei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^test$', views.test),
    url(r'^upload.htm$', views.upload),
    url(r'^tpl.html', views.tpl),
    # url(r'^add_user/$', views.add_user),
    # url(r'^del_user/$', views.del_user),
    # url(r'^edit_user/$', views.edit_user),
    # url(r'^edit_user-(?P<nnid>\d+).html$', views.edit_user_new),

]
