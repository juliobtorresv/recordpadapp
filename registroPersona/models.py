from django.db import models

# Create your models here.

class Persona(models.Model):
    cedula=models.CharField(max_length=13)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=15)
    representante=models.CharField(max_length=1)