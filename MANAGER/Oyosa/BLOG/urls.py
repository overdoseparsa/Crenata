from django.shortcuts import render 
from django.urls import path , include 
from django.http import HttpResponse
from .models import Post , User
def test_templates():
    "this is the function show the category list"
    pass




urlpatterns  = [
    path('test/' , lambda req : render(req , 'viewpost.html')) , 
    path('<str:Username>' , lambda req  , Username:HttpResponse(Post.objects.filter(author = User.objects.get(username = Username)))) , 

]