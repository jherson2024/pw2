from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    edad=models.IntegerField()
    donador=models.BooleanField()
    def get_abosolute_url(self):
        return reverse("personas:persona-detail",kwards={"pk":self.id})

class PersonaListView(ListView):
    model=Persona
    queryset=Persona.objects.filter(edad__lte="40")
