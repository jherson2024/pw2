from django.shortcuts import render
from django.views.generic import {
    ListView,
    DetailView,
    }

# Create your views here.
class PersonaListView(ListView):
    model=Persona
    queryset=Persona.objects.filter(edad__lte="40") 

class PersonaDetailView(DetailView):
    model=Persona
    # queryset=Persona.objects.filter(edad__lte="40") 