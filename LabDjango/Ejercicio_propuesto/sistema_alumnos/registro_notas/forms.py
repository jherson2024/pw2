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