import random

numeroAleatorio = random.randint(0,100)

print(numeroAleatorio)

print("Descubra o numero que foi escolhido pela maquina")
numeroUsuario = int(input())

print(numeroAleatorio)

while True:
    print("Descubra o numero que foi escolhido pela maquina")
    numeroUsuario = int(input())
    if numeroUsuario > numeroAleatorio:
        print("Um pouco menos")
    elif numeroUsuario < numeroAleatorio:
        print("Um pouco mais")
    else:
        print("BOA MLK !!!")
        break
