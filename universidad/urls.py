from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('carrera/nueva/', views.carrera_nueva, name='carrera_nueva'),
    ]