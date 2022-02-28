from django import template

register = template.Library()


@register.filter
def underslash(value):
    if value is not None:
        return value.replace('/', '_')
