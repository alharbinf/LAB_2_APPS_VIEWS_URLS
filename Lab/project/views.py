from django.shortcuts import render
from django.http import HttpResponse,HttpRequest


# Create your views here.

def my_fun(request):
    my_fun = ("Hello World, This is my new HOME !")
    return HttpResponse(f"{my_fun}")#my_fun here is the varable 
