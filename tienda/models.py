from django.db import models

# Create your models here.

class CategoríaProd(models.Model):
    nombre=models.CharField(max_length=20)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=20)
    categorias=models.ForeignKey(CategoríaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre