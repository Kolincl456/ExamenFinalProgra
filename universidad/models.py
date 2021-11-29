from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    alumno = models.ManyToManyField(Alumno, through='Asignacion')
    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(Carrera, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CarreraAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)