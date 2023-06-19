import random
usr = ''
while usr != "win":
    numeroMaquina = random.randint(0,2)
    if numeroMaquina == 0:
        numeroMaquina = "Pedra"
    elif numeroMaquina == 1:
        numeroMaquina = "Papel"
    else:
        numeroMaquina = "Tesoura"
    while True:
        print("---- VAMOS JOGAR PEDRA PAPEL OU TESOURA ----")
        print(f'1 = Pedra \n2 = Papel \n3 = Tesoura')
        usr = int(input("Diga um numero de 1 a 3: "))
        if usr == 1:
            usr = "Pedra"
            break