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

    def save(self,commit=True):
        nota_instance=super(NotaForm,self).save(commit=False)
        alumno_nombre=self.cleaned_data["alumno_nombre"]
        curso_nombre=self.cleaned_data["curso_nombre"]
        nota_instance.alumno=Alumno.objects.get(nombre=alumno_nombre)
        nota_instance.curso=Curso.objects.get(nombre=curso_nombre)
        if commit:
            nota_instance.save()
        return nota_instance