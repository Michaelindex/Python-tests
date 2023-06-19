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
        print("---- VAMOS JOGAR PEDRA PAPEL OU TESOURA ---