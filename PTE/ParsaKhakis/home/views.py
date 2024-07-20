from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 

def return_reponse_page(filename ,   data_context = {}):
    return HttpResponse(
        loader.get_template(filename).render(context=data_context)
    )
    

def start_page(req):
    return return_reponse_page('homepage.html')


def go_tho_home(req):
    return return_reponse_page('Home.html')
