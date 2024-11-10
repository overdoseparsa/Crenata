from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from typing import Any
import  django.contrib.auth.views  as DCAV
from django.http import HttpRequest
# my loggin 
# create decorator like django ninja 

class BaseViewLoggin(DCAV.LoginView):
    next_page = 'BLOG:account_page'
    data_cahce = []
    

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        print(self.data_cahce)
        
        
        return super().dispatch(request, *args, **kwargs)


    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        return super().get(request, *args, **kwargs)


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.data_cahce.append(request.POST)
        return super().post(request, *args, **kwargs)
# this is baseic from loggin vewis froms 
