import random
usr = int(input("Digite um numero de 1 a 100: "))
comp = random.randint(0,101)

while usr != comp:
    usr = int(input("Numero errado, digite o numero novamente: "))
    if usr > comp:
        print("Um pouco menos")
    else:
        print("Um pouco mais")

print("BOAA")