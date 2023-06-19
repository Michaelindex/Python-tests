import random
usr = ''
while usr != "win":
    numeroMaquina = random.randint(0,2)
    if numeroMaquina == 0:
        numeroMaquina = "Pedra"
    elif numeroMaquina == 1: