from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index2(request):
    return HttpResponse("<h1 style=color:green>welcome to home page</h1>")
