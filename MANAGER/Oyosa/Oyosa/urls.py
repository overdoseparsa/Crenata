# i want to add staticfile to projects 
"""
URL configuration for Oyosa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from debug_toolbar.toolbar import debug_toolbar_urls

'''
base urls conf user 

'''


urlpatterns = [
    path('admin/', admin.site.urls ),
    path('' , include('BLOG.urls' ,namespace='BLOG') , name="BlogUrls") , 
    path('tasks/' , include('tasks.urls') , name='tasks') ,   # this is for simple taskes 
    path('new/' , include('OYASALOG.acurls') , name='') , 
]
#add debugtoolbar
urlpatterns+= debug_toolbar_urls() #__debug__ 

