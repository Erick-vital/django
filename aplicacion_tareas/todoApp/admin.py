from django.contrib import admin

# Register your models here.

from .models import *

# codigo agrega la tabla 'Tareas' a nuestro admin
admin.site.register(Tareas)
