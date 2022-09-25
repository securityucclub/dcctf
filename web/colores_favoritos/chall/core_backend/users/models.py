from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuario = models.CharField(max_length=50, unique=True, null=False)
    contrasena = models.CharField(max_length=50, null=False)
    color_favorito = models.CharField(max_length=50, null=False)
