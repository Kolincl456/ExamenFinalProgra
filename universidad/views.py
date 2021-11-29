from django.shortcuts import render
from django.contrib import messages
from .forms import CarreraForm
from universidad.models import Carrera, Asignacion

def carrera_nueva(request):
    if request.method == "POST":
        formulario = CarreraForm(request.POST)
        if formulario.is_valid():
            carrera = Carrera.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'])
            for alumno in request.POST.getlist('alumno'):
                actuacion = Asignacion(alumno=alumno, asignacion = carrera.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Asignaciòn realizad exitosamente')

    else:
        formulario = CarreraForm()
    return render(request, 'universidad/carrera_editar.html', {'formulario': formulario})