from django import template
from ..models import Post
from taggit.models import Tag
register = template.Library()
# using json for optimization 
# using database manage ments to dont procecc again
# load links from projects 
# append data models to the first monitazers loaders 
@register.simple_tag # this is templates tags in python 
def count_hastack(values): # it is connet to the 
    print(values)
    print()
    return  Post.objects.filter(tags__in = [Tag.objects.get(slug=  values)]).count() # the COUNT OFF post returned
# this is the simple templates tags return the count of post objects # this is return by valueses # soo faar 
# whay it is not work parsa ??? 
#that register return the simple Query set 
# @register.simple_tag
# def get_comment_post():
#     pass
# when we render or use templaets tags 
from django.utils.safestring import mark_safe
import random
@register.simple_tag
def my_csrf_test_token():
    str_html = """ <input values = \' %s \' name='mycsrf' type = \'hidden\' >"""%random.random()
    return mark_safe(str_html)