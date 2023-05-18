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
        elif usr == 2:
            usr = "Papel"
            break
        elif usr == 3:
            usr = "Tesoura"
            break
        else:
            print("Numeros de um a três pls...")

    print("Você só saíra daqui se ganhar da maquina")
    if numeroMaquina == "Pedra" and usr == "Tesoura":
        print("A maquina venceu por escolher", numeroMaquina)
    elif numeroMaquina == "Papel" and usr == "Pedra":
        print("A maquina venceu por escolher", numeroMaquina)
    elif numeroMaquina == "Tesoura" and usr == "Papel":
        print("A maquina venceu por escolher", numeroMaquina)
    else:
        print("Você venceu por escolher:", usr, "x", numeroMaquina)
        usr = "win"



