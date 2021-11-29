from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('asignacion/nueva/', views.asignacion_nueva, name='asignacion_nueva'),
    ]