import random

usr = int(input("Digite um numero de 1 a 100: "))
comp = random.randint(0,101)

print(comp)
if usr != comp:
    print('MAOI')
