from django import forms
from .models import Alumno, Curso, Nota

class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields=['nombre']

class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields=["nombre"]

class NotaForm(forms.ModelForm):
    alumno_nombre=forms.CharField(label="Alumno")
    curso_nombre=forms.CharField(label="Curso")
    class Meta:
        model=Nota
        fields=["alumno_nombre","curso_nombre","nota"]