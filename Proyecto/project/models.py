from django.db import models

# Create your models here.
class contactanos(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    celular = models.CharField(max_length = 10)
    email = models.EmailField()
    