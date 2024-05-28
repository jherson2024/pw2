from django.db import models
from django import models

# Create your models here.
class Persona(models.Model):
    nombres=models.TextField()
    apellidos=models.TextField()
    edad=models.TextField()