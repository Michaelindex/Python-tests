from django.contrib import admin
from .models import Lanche
# Register your models here.
class ListaLanche(admin.ModelAdmin):
    list_display = ('id','nome','categoria','preco') 
    list_display_links = ('id','nome',) 
    search_fields = ('nome',) 
    list_filter = ('categoria',) 
    list_per_page = 3


admin.site.register(Lanche, ListaLanche)

