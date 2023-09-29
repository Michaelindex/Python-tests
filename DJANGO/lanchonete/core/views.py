from django.shortcuts import render, get_object_or_404
from lanche.models import Lanche
from django.db.models import Q
from django.core.paginator import Paginator #Paginação
# Create your views here.
def index(requests):
    #lanches = Lanche.objects.all() # SELECT * FROM lanche
    lanches = Lanche.objects.order_by('-date_lanche').filter(publicado=True)
    paginator = Paginator(lanches, 9) #Paginação
    page = requests.GET.get('pagina') #Paginação
    lanches = paginator.get_page(page) #Paginação
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
        print( (f'Conteúdo da caixa de busca: {nome_a_buscar}'))
        if nome_a_buscar: 
            lanches = lanches.filter(Q(nome__icontains=nome_a_buscar) | Q(categoria__icontains=nome_a_buscar) | Q(ingredientes__icontains=nome_a_buscar))
    dados = {
        'lista_lanches' : lanches
    } 
    return render(requests, 'buscar.html', dados)