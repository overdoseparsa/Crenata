from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 

def start_page(request):
    data_context = {}
    temp = loader.get_template('homepage.html')
    return HttpResponse(
        temp.render(context=data_context)
    )
