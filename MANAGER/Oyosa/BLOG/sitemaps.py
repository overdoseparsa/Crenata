from django.contrib.sitemaps import Sitemap
from .models import Post # this is simple Post from models 

class PostSitemap(Sitemap):
    changefreq  = 'weeky'
    priority = 0.9
    def items(self):
        return Post.objects.all()
    
    def lasemod(self , obj) : 
        return obj.updated