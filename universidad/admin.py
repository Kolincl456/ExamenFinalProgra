from typing import Callable
from django.contrib import admin

from universidad.models import Alumno, AlumnoAdmin, Carrera, CarreraAdmin

admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Carrera, CarreraAdmin)