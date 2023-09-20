from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('lanche/<int:lanche_id>', lanche, name='lanche'),       
]
