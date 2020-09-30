from django.db import models

# Create your models here.
""" ---guardar cambios a tus modelos---
    cada cambio realizado a modelos se guardan
    con los sig comandos en la terminal.
    >python manage.py makemigrations nombreApp
    >python manage.py migrate 
"""


class Tareas(models.Model):
    titulo_tarea = models.CharField(max_length=20)
    marcado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo_tarea

