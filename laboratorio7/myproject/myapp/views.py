from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

# def home(request):
#     return render(request,'index.html',{"day":30})  

def add(request):   
    val1=int(request.POST['num1'])   
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{"result":res}) 

def home(request):

    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The city that never sleeps"
    dest1.img="destination_1.jpg"
    dest1.price=700

    dest2=Destination()
    dest2.name="Hiderabab"
    dest2.desc="Not recomendable"
    dest2.img="destination_2.jpg"
    dest2.price=400

    dest3=Destination()
    dest3.name="Bengaluru"
    dest3.desc="Beautiful"
    dest3.img="destination_3.jpg"
    dest3.price=800    

    dests=[dest1,dest2,dest3]

    return render(request, 'index.html', {'dests': dests})  

def home2(request):

    dests=Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})  