from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html',{"name":"Navin"})  

def add(request):   
    val1=request.GET["num1"]
    val2=request.GET["num2"]
    res=val1+val2
    return render(request,'result.html',{"result":res})   