from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("<h1 style=color:red>welcome to home page</h1>")
