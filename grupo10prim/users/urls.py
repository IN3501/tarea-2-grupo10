from django.urls import path
from .views import *

urlpatterns = [
    path('registrar_usuario', registrar_usuario, name='registrar_usuario'),
    path('mostrar_resultado', recuperar_registro, name='mostrar_resultado')
]