#from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import VentaForm
from .models import Venta
from .models import Movie

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:  # Manejar la solicitud GET
        form = VentaForm()  # Crea un formulario vacío
    return render(request, 'tienda/crear_venta.html', {'form': form})

def lista_ventas(request):
  ventas = Venta.objects.all()
  return render(request, 'tienda/lista_ventas.html', {'ventas': ventas})

def lista_peliculas(request):
  return render(request, 'tienda/lista_peliculas.html')

def prueba(request):
  return render(request, 'tienda/prueba.html')

def movie_list(request):
    if request.method == 'GET':
        print("Obteniendo datos de películas...")
        movies = Movie.objects.all()
        print("Películas obtenidas:", movies)
        movie_data = list(movies.values())  # Convierte los objetos de película en una lista de diccionarios
        print("Datos de películas formateados:", movie_data)
        return JsonResponse(movie_data, safe=False)
    else:
        print("Método no permitido")
        return JsonResponse({'error': 'Método no permitido'}, status=405)