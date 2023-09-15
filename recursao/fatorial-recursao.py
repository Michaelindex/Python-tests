def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)
numero = int(input('Informe um número inteiro: '))
if numero >= 0:
    print(fatorial(numero))
else:
    print('Números negativos não são permitidos!')