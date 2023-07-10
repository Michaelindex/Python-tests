import random

def adivinhar_numero():
    comp = random.randint(1, 100)
    tentativas = 0

    while True:
        usr = int(input("Digite um número de 1 a 100: "))
        tentativas += 1

        if usr > comp:
            print("Um pouco menos")
        elif usr < comp:
            print("Um pouco mais")
        else:
            print("BOAA! Você acertou em", tentativas, "tentativa(s)!")
            break

adivinhar_numero()
