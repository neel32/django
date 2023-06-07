# This file add by me = Neel

from django.http import  HttpResponse

def index(request):
    return HttpResponse("Hello World")