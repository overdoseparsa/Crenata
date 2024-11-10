from django.contrib import admin

# Register your models here.
from .models import Post  , Category    , Followers , Following , Transmisson  , USERTOKENUDDD
# createed models admin for all models 

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Followers)
admin.site.register(Following)
admin.site.register(
Transmisson
)

admin.site.register(
USERTOKENUDDD
)
