from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('clinicas', views.clinicas, name='clinicas'),
    path('listado', views.listado, name='listado'),
]
