from django.shortcuts import render 
from django.urls import path , include 
from .views import AcViews 
TEST_RENDER = lambda requests : render(requests , 'profile.html')
# render from templaets 


urlpatterns  = [
    path('<str:Username>' ,AcViews.as_view() , name="get_post") , 
    path('test/' , TEST_RENDER , name = 'testing')    
]
