from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=200)
    oferta = models.BooleanField(default=False)
    
    def tachado(self):
        if self.oferta:
            return "$"+str(round(self.precio * 1.2))
        else:
            return ""
    
    def __str__(self):
        return self.codigo+" - "+self.descripcion

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    estado = models.CharField(max_length=20, default="EN PREPARACION")
    
    def __str__(self):
        return str(self.id)+" "+str(self.fecha)

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()
    
    
    def __str__(self):
        return str(self.id)+" "+self.producto.codigo