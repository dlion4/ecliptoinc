# filters.py

from django import template

register = template.Library()


@register.filter
def to_list(value):
    return list(value)
