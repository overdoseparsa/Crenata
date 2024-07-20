from django.urls import path , include
from django.urls.resolvers import URLPattern
from django.shortcuts import  HttpResponse
from .views import start_page
# this is connectd to the templates and usring somthins
urlpatterns = [
    path('' , start_page  , name='home page')
]
