from django.shortcuts import render 
from django.urls import path , include 
from .views import AccountPreviews , page_start  , like_post
TEST_RENDER = lambda requests : render(requests , 'post.html')
# render from templaets 

# appends/fromdisapp 
urlpatterns  = [
    # path('test/' , TEST_RENDER , name = 'testing')  ,
    path('<str:username>' , page_start , name="account_page") , 
    # it have to be api but here  get 
    path('<int:post_id>/like' , like_post,  name = 'like_post')

]
