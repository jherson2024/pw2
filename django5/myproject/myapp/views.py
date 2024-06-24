from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Persona

# Lista de Personas
class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte=40)

# Detalle de una Persona
class PersonaDetailView(DetailView):
    model = Persona

# Creación de una nueva Persona
class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        "nombres",
        "apellidos",
        "edad",
        "donador",
    ]

# Actualización de una Persona
class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        "nombres",
        "apellidos",
        "edad",
        "donador",
    ]

# Eliminación de una Persona
class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')

# Vista personalizada con respuesta HTTP
class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hola mundo con Clases')