from django.urls import path
from .views import *

urlpatterns = [
    path('', homeCliente, name='homeCliente'),
    path('inputs/', inputs, name='inputs'),
    path('contacto', contacto, name='contacto'),
    path('agenda', agenda, name='agenda'),
    path('catalogo', catalogo, name='catalogo'),

    path('backoffice', backoffice, name='backoffice'),
    path('homeEmpresa', homeEmpresa, name='homeEmpresa'),
    path('fichaClinica', fichaClinica, name='fichaClinica'),
    path('estadisticas', estadisticas, name='estadisticas'),
    path('inventario', inventario, name='inventario'),
    path('comprar', comprarObjeto, name='comprarObjeto')
]
