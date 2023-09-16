fatorial = int(input("Informe um número inteiro: "))
abc = 1
for a in range(fatorial):
    abc = abc * (a+1)
print(abc)

num = int(input("Digite um numero: "))
conta = 1
for i in range(1, num+1):
    conta *= i
print(conta)