from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
""" importar modelos 'models'
    el punto en '.models' significa que es un 
    archivo hermano de la misma carpeta
"""
from .models import Tareas
#importar formularios
from .forms import Formulario_tareas

# Create your views here.

def index(request):
    #alamzena tabla en variable
    tareas = Tareas.objects.all()
    #importa el formulario
    form_tarea = Formulario_tareas()
    if request.method == 'POST':
        form_tarea = Formulario_tareas(request.POST)
        if form_tarea.is_valid():
            form_tarea.save()
        return redirect('/todoApp')


    """ crea el contexto de nuestra pagina
        como primer argumento la tabla
        'tareas'
    """
    contexto = {'tareas':tareas,
    'form_tarea':form_tarea}

    return render(request, 'index.html',
    contexto)

def borrar_tarea(request, tarea_id):
    tarea_item = Tareas.objects.get(id=tarea_id)
    tarea_item.delete()
    
    return HttpResponseRedirect('/todoApp')