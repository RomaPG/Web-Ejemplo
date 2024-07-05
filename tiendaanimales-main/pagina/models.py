# models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    rut = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=100)  # Considera usar un campo de contraseña seguro en producción
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
