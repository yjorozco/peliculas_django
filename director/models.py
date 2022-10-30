from django.db import models

# Create your models here.


class Director(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    director =  models.ForeignKey(Director, on_delete = models.RESTRICT)
    def __str__(self):
        return self.nombre