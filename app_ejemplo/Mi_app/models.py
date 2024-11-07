from django.db import models

class Ejemplo(models.Model):
    texto = models.TextField()

def __str__(self):
        return self.texto



