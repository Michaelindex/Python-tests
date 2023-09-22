from django.contrib import admin
from .models import Funcionario
# Register your models here.
class ListaFuncionario(admin.ModelAdmin):
    list_display = ('id','nome','email') 
    list_display_links = ('id','nome','email') 
    search_fields = ('nome', 'funcao', 'email')
    list_filter = ('funcao',)  
    list_per_page = 3


admin.site.register(Funcionario, ListaFuncionario)