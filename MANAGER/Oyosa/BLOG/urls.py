from django.shortcuts import render  , HttpResponse 
from django.urls import path , include 
import os 
from django.http import HttpRequest
# we add BASE DIR TO PATH 
from .views import account_page , AccountPreviews , page_start  , like_post , post_page , postings_froms , comment_views ,get_post_by_account
TEST_RENDER = lambda requests : render(requests , 'post.html') 
app_name = 'BLOG'
# create the api 
# login 
TEST_NA_HASH = lambda Httprequests :  render(Httprequests, 'hashtakpost.html')
api_patterns = [
    path('User/post'  , view=get_post_by_account ) # this is api 
    
]

from .views import sign_in ,test_csfr_my_self , show_MEHTOD  , loggin_user, hash_tak_post , test_my_csrf_token , logout_user
from .sitemaps import PostSitemap 
from django.contrib.sitemaps.views import sitemap
sitemaps = {
'posts': PostSitemap,
}

from .feed import LatestPostsFeed
from .views import search_from_post
from django.contrib.auth import login , logout


urlpatterns  = [
    path('' , page_start , name="account_page") , # this is main mrapper
    path('<str:Username>' ,account_page , name='User_accounts') , 
    # path('test/' , TEST_RENDER , name = 'testing')  ,
    path('loggin/' , loggin_user , name='loggin_page') , 
    path('logout/' , logout_user , name ='logout') , 
    path('signin/' ,sign_in , name ='sign_in') , 
    path('<str:Username>/show/<slug:tagsurls>' , page_start , name="account_page_tags") , # this is main uses 
    # we add this to the maker down 
    path('post/' ,post_page  , name='post_user' ) , 
    path('<str:Username>/posting' ,postings_froms  , name='posting_user' )  , 
    path('<str:Username>/<int:post_id>/comment' , comment_views , name = 'comment_post') , # POST  # inline requests
    path('<int:post_id>/like' , like_post,  name = 'like_post') , 
    path('<Username>/test' , test_csfr_my_self) , 
    path('api/' ,include(api_patterns) )  , # it is include to the api urls 
    path('show/' , show_MEHTOD , ) , 
    path('test/' , TEST_NA_HASH , name="test"), 
    path('hash/<slug:slug>',hash_tak_post , name='HASHPOST' ) , 
    path('test/testcsrf' , test_my_csrf_token , name='TEST_CSRF') ,  # this is test my csrf tokens 
    path(
        's/sitemap.xml'  ,
        sitemap , 
        {'sitemaps':sitemaps} , 
        name='django.contrib.sitemaps.views.sitemap'
    ) ,  # this is for sitemap 

        path('feed/feed/', LatestPostsFeed(), name='post_feed'),
    path('post/search' ,search_from_post , name="search_Post") , 
    

    # path('new/' , include('django.contrib.auth.urls'))
]
# this is progblem for us from rkinterususer 
