# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Blog Home")

def food(request):
    return HttpResponse("Blog/Food Home")


def editor(request):
    if request.user.is_authenticated:
        return HttpResponse("Blog/Editor Home")
    else:
        return HttpResponse("Go back") 
   
