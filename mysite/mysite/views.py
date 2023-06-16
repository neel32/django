# This file add by me = Neel

from django.http import  HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse(" About Hello World")

def index(request):
    params = {'name' : 'Neel', 'place': 'USA'}
    return render(request, 'index.html', params)
    # return HttpResponse("Home")
def removepunc(request):
    djtext = request.GET.get('text', 'default')
    return HttpResponse(" Remove Punc")
def capfirst(request):
    return HttpResponse("Capitalize First")
def newlineremove(request):
    return HttpResponse("New Line Remove")
def spacefirst(request):
    return HttpResponse("Space First <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("Char Counnt")
