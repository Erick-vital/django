from django import forms
from django.forms import ModelForm
from .models import Tareas

""" este modulo permite crear formularios a 
    partir de los modelos, para una mejor 
    manupulacion.

    Para mas informacion visita:
    https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
"""

#formulario django
class Formulario_tareas(forms.ModelForm):

    class Meta:
        #tabla o 'modelo' a importar
        model = Tareas
        """ campos a importar de nuestros modelo
            en este caso importaremos todo, pero
            tambien puedes crear una lista y
            espesificar que importar
        """
        fields = '__all__'