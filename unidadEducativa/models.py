from django.db import models

# Create your models here.

class UnidadEducativa(models.Model):
    ruc=models.CharField(max_length=15)
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=15)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=15)
    