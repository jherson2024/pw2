from django.db import models
from django.urls import reverse

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def get_absolute_url(self):
        return reverse("personas:persona-detail", kwargs={"pk": self.id})


