from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('lanche/<int:lanche_id>', lanche, name='lanche'),
    path('buscar', buscar, name='buscar')        
]
