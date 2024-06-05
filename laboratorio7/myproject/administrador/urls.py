from django.urls import path
from . import views

urlpatterns=[
    path("administrar",views.administrar,name="administrar"),
    ]