from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse('<h1>柴颖颖最美!</h1>')
