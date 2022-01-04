from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Sindhu Team - How are you ? !")
