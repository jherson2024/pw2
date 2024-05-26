"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#esto agrege
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #esto puse
    
]

#y esto mas agrege
urlpatterns = [
    path('crear/', views.crear_venta, name='crear_venta'),
    path('', views.lista_ventas, name='lista_ventas'),
    path('lista_peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('prueba/', views.prueba, name='prueba'),
    path('movies/', views.movie_list, name='movie_list')
]

