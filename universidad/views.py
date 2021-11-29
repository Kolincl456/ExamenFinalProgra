from django.shortcuts import render

from django.contrib import messages
from .forms import PeliculaForm
from universidad.models import Carrera, Asignacion


def asignacion_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            pelicula = Carrera.objects.create(nombre=formulario.cleaned_data['nombre'])
            for actor_id in request.POST.getlist('actores'):
                actuacion = Asignacion(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Asignaciòn realizad exitosamente')

    else:
        formulario = PeliculaForm()
    return render(request, 'asignacion/asignacion_editar.html', {'formulario': formulario})