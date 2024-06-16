from django.urls import path
from . import views

urlpatterns = [
    path('', views.myHomeView, name='myHomeView'),
    path('persona/',views.personaTestView,name='testViewPersona'),
    path('agregar/',views.personaCreateView,name='createPersona'),
    path('search/',views.searhForHelp,name='buscar'), 
]