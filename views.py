from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
""" def index(request):
    return HttpResponse("Hey! This is i am") """
def index(request):
    people={
"name":"John",
"age":30,
"city":"New York",
"Title":"Django Developer",
    }
    
    return render(request,"index.html",context={'people':people})
def success(request):
    return HttpResponse("Hey! This is success page")