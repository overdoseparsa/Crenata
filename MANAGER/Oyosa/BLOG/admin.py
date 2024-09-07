from django.contrib import admin

# Register your models here.
from .models import Post  , Category    , Followers , Following

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Followers)
admin.site.register(Following)
