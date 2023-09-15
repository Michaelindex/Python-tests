from os import system, name

import random

opcao = 's'
while opcao.upper()=='S':
    system('cls') if (name=='nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opcao para se jogar:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))

    pecas = ("Padra", "Papel", "Tesoura")

    if(jogador > 2):
        resultado = "Você não escolheu um item correto !!!"
    else:
        print('Voce escolheu {}' . format(pecas[jogador]))
        print('O computador escolheu: {}' . format(pecas[computador]))
        tabela = ((0,1,-1),(-1,0,1),(1,-1,0))
        jogada = tabela[computador][jogador]
        resultado=(
            "Deu empate vocês escolhem a mesma peça",
            "Você ganhou!",
            "O computador ganhou"
        )

    print(resultado[jogador])
    opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente.')