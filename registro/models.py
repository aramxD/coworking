from django.db import models

# Create your models here.
class registro(models.Model):
    #Datos generales
    nombre = models.CharField(max_length=30)
    apeido = models.CharField(max_length=30)
    telefono  = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre