from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Alumno(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Notas(models.Model):
    alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(20)])

    def __str__(self):
        return f"{self.alumno}-{self.curso}:{self.nota}"