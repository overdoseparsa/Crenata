from django.urls import path , include
from django.urls.resolvers import URLPattern
from django.shortcuts import  HttpResponse
# this is connectd to the templates and usring somthins
urlpatterns = [
    path('' , lambda req : HttpResponse("this page not hellow ".title())  , name='home page ')
]
