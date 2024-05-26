from .models import Alumno, Curso, Nota
from .forms import AlumnoForm, CursoForm, NotaForm
from django.shortcuts import redirect, render

# Create your views here.
def pagina(request):
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
                nota_form.save()
                return redirect("pagina_principal")
    
    return render(request, "registro_notas/index.html", {
        "alumno_form":alumno_form,
        "curso_form":curso_form,
        "nota_form":nota_form,
    })