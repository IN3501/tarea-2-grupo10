from django.urls import path
from .views import *

urlpatterns = [
    path('registrar_usuario', registrar_usuario, name='registrar_usuario'),
]