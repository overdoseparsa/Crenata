from django.shortcuts import render 
from django.urls import path , include 
from .views import AcViews 



urlpatterns  = [
    path('<str:Username>' ,AcViews.as_view() , name="get_post")
    
    
]