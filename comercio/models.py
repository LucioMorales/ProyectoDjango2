from django.db import models

# Create your models here.

class Producto():
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    precio=models.FloatField()
    stock=models.IntegerField()

    def __str__(self):
        return str(self.nombre)

class Categoria():
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    nombre=models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.nombre)
class Proveedor():

class Cliente():

class Direccion():

class Detalle():

class Venta():

