from django.shortcuts import render
from django.views.generic import {
    ListView,
    DetailView,
    CreateView,
    Update,
    Delete,
    }

# Create your views here.
class PersonaListView(ListView):
    model=Persona
    queryset=Persona.objects.filter(edad__lte="40") 

class PersonaDetailView(DetailView):
    model=Persona
    # queryset=Persona.objects.filter(edad__lte="40") 

class PersonaCreateView(CreateView):
    model=Persona
    fields=[
        "nombres",
        "apellidos",
        "edad",
        "donador",
    ]
class PersonaUpdateView(UpdateView):
    model=Persona
    fields=[
        "nombres",
        "apellidos",
        "edad",
        "donador",
    ]

class PersonaDeleteView(DeleteView):
    model=Persona
    succes_url=reverse_lazy('personas:persona-list')
