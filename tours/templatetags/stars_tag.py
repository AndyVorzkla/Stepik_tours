from django import template

register = template.Library()


@register.filter()
def stars(value, arg=None):
    """Return count of stars"""
    stars = int(value)
    return '★' * stars
