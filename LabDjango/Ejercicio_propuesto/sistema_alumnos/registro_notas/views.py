from .models import Alumno, Curso, Nota
from .forms import AlumnoForm, CursoForm, NotaForm

# Create your views here.
def pagina(request):
    alumno_form=AlumnoForm()
    curso_form=CursoForm()
    nota_form=NotaForm()

    if request.method=="POST":
        if "alumno_submit" in request.POST:
            alumno_form=AlumnoForm(request.POST)
        if "curso_submit" in request.POST:
            curso_form=AlumnoForm(request.POST)
        if "nota_submit" in request.POST:
            nota_form=AlumnoForm(request.POST)