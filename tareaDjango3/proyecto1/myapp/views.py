from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
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
    return render(request,"personas/descripcion.html",context)

def personaCreateView(request):
    print(request)
    if request.method=="POST":
        nombre=request.POST.get("q")
        print(nombre)
    context={}
    return render(request,"personas/personasCreate.html",context)

def searchForHelp(request):
    return render(request,"personas/search.html",{})