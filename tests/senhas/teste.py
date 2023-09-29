import random
import pyperclip
import string

def randomizarint():
    tamanho = 12
    senha = ''
    for i in range(tamanho):
        senharamdom = random.randint(1,9)
        senha = str(senha + str(senharamdom))
    pyperclip.copy(senha)

#randomizarint()

def randomizarstr():
    letras = string.ascii_letters
    