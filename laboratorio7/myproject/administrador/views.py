from django.shortcuts import render, redirect
from myapp.models import Destination
from .forms import CrearForm, EliminarForm

# Create your views here.
def administrar(request):
    crear_form=CrearForm()
    eliminar_form=EliminarForm()

    if request.method=="POST":
        if "crear_submit" in request.POST:
            crear_form=CrearForm(request.POST)
            if crear_form.is_valid():
                crear_form.save()
                return redirect("administrar")
        elif "eliminar_submit" in request.POST:
            eliminar_form=EliminarForm(request.POST)
            if eliminar_form.is_valid():
                name_destino=eliminar_form.cleaned_data['name']
                Destination.objects.filter(name=name_destino).delete()
                return redirect("administrar")            
    
    lista=Destination.objects.all()
    return render(request, "administrar.html", {
        "crear_form":crear_form,
        "eliminar_form":eliminar_form,
        "lista":lista,
    })