# This file add by me = Neel

from django.http import  HttpResponse

# def index(request):
#     return HttpResponse('''<h2>Hello World</h2>
#     <a href="https://www.youtube.com/watch?v=oXN2q7MjxGo">Song Time</a>''')
def about(request):
    return HttpResponse(" About Hello World")

def index(request):
    return HttpResponse("Home")
def removepunc(request):
    return HttpResponse(" Remove Punc")
def capfirst(request):
    return HttpResponse("Capitalize First")
def newlineremove(request):
    return HttpResponse("New Line Remove")
def spacefirst(request):
    return HttpResponse("Space First")
def charcount(request):
    return HttpResponse("Char Counnt")
