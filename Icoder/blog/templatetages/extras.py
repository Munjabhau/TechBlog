from django import template
from ..models import Post
from ..models import BlogComment
register=template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)