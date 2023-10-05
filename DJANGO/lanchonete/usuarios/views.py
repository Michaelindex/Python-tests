from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from lanche.models import Lanche
from django.core.paginator import Paginator
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request,'Os campos email e senha não podem ficar em branco' )
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list( 'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user) 
                messages.success(request,'Login realizado com sucesso') 
                return redirect('dashboard')
            else:
                messages.error(request,'A senha está incorreta!' )      
        else:
            messages.error(request,'Digite um e-mail válido' )        
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'cadastro.html')
    return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        lanche = Lanche.objects.order_by('-date_lanche').filter(usuario=id)
        paginator = Paginator(lanche, 9) 
        page = request.GET.get('page') 
        lanche = paginator.get_page(page)
        dados = { 'lista_lanches' : lanche }
        return render(request, 'dashboard.html', dados)

def logout(request):
    auth.logout(request)
    return redirect('index')

def cria_lanche(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        categoria = request.POST['categoria']
        ingredientes = request.POST['ingredientes']
        foto_lanche = request.FILES['foto_lanche']
        user = get_object_or_404(User, pk=request.user.id)
        lanche = Lanche.objects.create(usuario=user, nome=nome, preco=preco, ingredientes=ingredientes, categoria=categoria, foto_lanche=foto_lanche)
        lanche.save()
        return redirect('dashboard')
    else:
        return render(request, 'cria_lanche.html')

def deleta_lanche(request):
    pass

def edita_lanche(request):
    pass

def atualiza_lanche(request):
    pass
