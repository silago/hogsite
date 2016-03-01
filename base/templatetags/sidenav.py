from base.models import * 
from django import template

register = template.Library()

@register.simple_tag()
def sidenav():
    items  =  BlogEntry.objects.filter(pinned=True)
    return items


