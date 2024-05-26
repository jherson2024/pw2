from .models import Alumno, Curso, Nota
from .forms import AlumnoForm, CursoForm, NotaForm
from django.shortcuts import redirect, render

# Create your views here.
def pagina_principal(request):
    alumno_form=AlumnoForm()
    curso_form=CursoForm()
    nota_form=NotaForm()

    if request.method=="POST":
        if "alumno_submit" in request.POST:
            alumno_form=AlumnoForm(request.POST)
            if alumno_form.is_valid():
                alumno_form.save()
                return redirect("pagina_principal")
        if "curso_submit" in request.POST:
            curso_form=CursoForm(request.POST)
            if curso_form.is_valid():
                curso_form.save()
                return redirect("pagina_principal")
        if "nota_submit" in request.POST:
            nota_form=NotaForm(request.POST)
            if nota_form.is_valid():
                try:
                    instancia=nota_form.save(commit=False)
                    alumno_nombre=nota_form.cleaned_data["alumno_nombre"]
                    curso_nombre=nota_form.changed_data["curso_nombre"]
                    instancia.alumno=Alumno.objects.get(nombre=alumno_nombre)
                    instancia.curso=Curso.objects.get(nombre=curso_nombre)
                    instancia.save()
                except Alumno.DoesNotExist:
                    nota_form.add_error("alumno_nombre","El alumno no existe en los registros")
                except Curso.DoesNotExist:
                    nota_form.add_error("curso_nombre","El curso no existe")
                else:
                    return redirect("pagina_principal")
    
    return render(request, "registro_notas/index.html", {
        "alumno_form":alumno_form,
        "curso_form":curso_form,
        "nota_form":nota_form,
    })