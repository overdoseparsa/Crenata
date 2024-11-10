from django.urls import path
from django.http import JsonResponse
# we need here token keys
urlspatterns = [
    path('test/' , lambda requests:JsonResponse({'status':'ok'}))
]
