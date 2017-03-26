from django.contrib import admin

from bbs import models

# Register your models here.


admin.site.register(models.Article)
admin.site.register(models.UserProifle)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.PrivateMail)
admin.site.register(models.Category)
