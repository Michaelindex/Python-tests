from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'), 
    path('dashboard', dashboard, name='dashboard'), 
    path('logout', logout, name='logout'),
    path('cria-lanche', cria_lanche, name='cria_lanche'),
    path('deleta/<int:lanche_id>', deleta_lanche, name='deleta_lanche'),
    path('edita/<int:lanche_id>', edita_lanche, name='edita_lanche'),
    path('atualiza_lanche', atualiza_lanche, name='atualiza_lanche')
]
