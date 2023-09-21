from django.shortcuts import render, get_object_or_404
from lanche.models import Lanche

# Create your views here.
def index(requests):
    lanches = Lanche.objects.all() # SELECT * FROM lanche
    dados = { 'lista_lanches':lanches }
    return render(requests, 'index.html', dados)

def contato(requests):
    return render(requests, 'contato.html')

def lanche(requests, lanche_id):
    lanche = get_object_or_404(Lanche, pk=lanche_id)
    lanche_a_exibir = { 'lanche':lanche}
    return render(requests, 'lanche.html', lanche_a_exibir)

def buscar(requests):
    lanches = Lanche.objects.order_by('-date_lanche').filter(publicado=True)
    if 'buscar' in requests.GET:
        nome_a_buscar = requests.GET['buscar']

        if nome_a_buscar:
            lanches = lanches.filter(nome__icontains=nome_a_buscar)
    dados = {
        'lista_lanches' : lanches
    }
    return render(requests, 'buscar.html', dados)