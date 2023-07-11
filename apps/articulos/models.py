from django.db import models
from django.utils import timezone
# Create your models here.

#Categoria
class Categoria(models.Model):

    nombre = models.CharField(max_length=200, null=False)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

