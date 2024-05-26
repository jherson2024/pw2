from .models import Alumno, Curso, Nota
from .forms import AlumnoForm, CursoForm, NotaForm

# Create your views here.
def pagina(request):
    alumno_form=AlumnoForm()
    curso_form=CursoForm()
    nota_form=NotaForm()