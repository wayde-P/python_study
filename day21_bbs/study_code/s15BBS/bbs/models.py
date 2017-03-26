from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class UserProifle(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey("UserProifle")
    category = models.ForeignKey("Category")
    pub_date = models.DateTimeField(auto_now_add=True, auto_created=True)
    tags = models.ManyToManyField("Tag", null=True)
    body = models.TextField(max_length=100000)
    head_img = models.ImageField(upload_to="uploads")
    status_choices = ((0, '草稿'), (1, '发布'), (2, '隐藏'))
    priority = models.SmallIntegerField(default=1000, verbose_name="优先级")

    def __str__(self):
        return self.title


class Category(models.Model):
    """板块"""
    name = models.CharField(max_length=64, unique=True)
    set_as_top_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """评论"""
    article = models.ForeignKey("Article")
    p_node = models.ForeignKey("Comment", null=True, blank=True, related_name="my_child_comments")

    user = models.ForeignKey("UserProifle")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1024)

    def __str__(self):
        return self.comment


class Like(models.Model):
    """点赞"""
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProifle")
    date = models.DateTimeField(auto_now_add=True)


class PrivateMail(models.Model):
    """私信"""
    pass
