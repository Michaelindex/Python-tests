from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, "Os Campos email e senha não podem ficar")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list( 'username', flat=True).get()
            user = auth.authenticate(request, username=nome, poassword=senha)
            print(nome, user)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request,'A senha está incorreta!')
        else:
            messages.error(request, 'Digite um e-mail válido!')
    return render(request, 'login.html')

def cadastro(request):
    pass

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        lanche = Lanche.objects.order_by('-date_lanche').filter(usuario=id)
        paginator = paginator(lanche, 9)
        page = request.GET.get('page')
        lanche = paginator.get_page(page)
        dados = { 'lista_lanches' : lanche }
        return render(request, 'dashboard.html', dados)

def logout(request):
    pass

def cria_lanche(request):
    pass

def deleta_lanche(request):
    pass

def edita_lanche(request):
    pass

def atualiza_lanche(request):
    pass
