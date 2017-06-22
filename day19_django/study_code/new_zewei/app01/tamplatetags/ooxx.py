from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def ji(value, num):
    return 'jiji-->' + str(num) + value


@register.filter
def ya(value, v):
    temp = '<a href="http://www.baidu.com/?t=%s">%s</a>' % (v, value)
    return mark_safe(temp)
