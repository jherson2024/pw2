from django import forms
from myapp.models import Destination

class CrearForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields=['name','img','desc','price','offer']

class EliminarForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields=["name"]

