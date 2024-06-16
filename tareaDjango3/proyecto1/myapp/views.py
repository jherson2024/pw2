from django.shortcuts import render
from .models import Persona
# Create your views here.
def myHomeView(request,*args,**kwargs):
    myContext={
        "myText":"Esto es sobre nosotros",
        "myNumber":123,
        "myList":[33,44,55],
    }
    return render(request,"home.html",myContext)

def personaTestView(request):
    obj=Persona.objects.get(id=1)
    context={
        "objeto":obj,
    }
    return render(request,"test.html",context)