from django.shortcuts import render
from django.views import View
from django.http import HttpResponse , HttpResponseBadRequest
from .models import Post , User
# Create your views here.

class AcViews(View): # this is classed base views 
    act_views = 0 
    templates_for_get_page = "post.html"
     
    def get(self , requests:HttpResponse , Username):
        if AcViews.act_views == 100 :
            return HttpResponseBadRequest("your requets is not permisions ")
        context = {
            'posts':Post.objects.filter(
                author = User.objects.get(username = Username)
            )
        }   
        AcViews.act_views += 1 
        print(AcViews.act_views)
        return render(requests , AcViews.templates_for_get_page , context=context)    


# this is the view from the post accoutns 


