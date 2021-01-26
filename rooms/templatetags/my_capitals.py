from django import template

register = template.Library()


@register.filter
def my_capitals(value):
    print(value)
    return "lalalalalala"