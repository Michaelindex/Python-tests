import random
import pyperclip
import string

def randomizar():
    tamanho = 12
    senha = ''
    for i in range(tamanho):
        senharamdom = random.randint(1,9)
        senha = str(senha + str(senharamdom))
        print(senha)

randomizar()