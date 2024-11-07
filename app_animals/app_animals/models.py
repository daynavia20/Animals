from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.IntegerField()
    habitat = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")
    
    def __str__(self):
        return self.nombre

