from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre=models.CharField(max_length=20,)
    correoelectronico=models.EmailField(unique=True)
    usuario=models.CharField(max_length=20,unique=True)
    contraseña=models.CharField(max_length=20)
    fechadenacimiento=models.DateField(auto_now=False)
    nacionalidad=models.CharField(max_length=20,)