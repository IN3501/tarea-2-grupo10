from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	
]