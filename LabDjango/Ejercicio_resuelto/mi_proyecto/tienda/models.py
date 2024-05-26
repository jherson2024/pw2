from django.db import models

class Producto(models.Model):
  codigo = models.CharField(max_length=100, unique=True)
  nombre = models.CharField(max_length=200)
  descripcion = models.TextField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  def __str__(self):
    return self.nombre

class Venta(models.Model):
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  cantidad = models.PositiveIntegerField()
  fecha = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"Venta de {self.cantidad} unidades de {self.producto.nombre}"

class Movie(models.Model):
    MovieID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=100)
    Year = models.IntegerField(default=0)
    Score = models.FloatField(default=0.0)  # Establece un valor predeterminado aquí
    Votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Title
    class Meta:
        managed = False
        db_table = 'Movie' 