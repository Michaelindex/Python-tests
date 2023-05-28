print("")
print("")

print("Loja do Johnata Suzarte Souza (RU:3996609)")
print("")
valor_unitario = float(input("Digite o valor unitário do produto: "))  # Solicita ao usuário o valor unitário do produto e armazena como um número decimal (float)

quantidade = int(input("Digite a quantidade do produto: "))  # Solicita ao usuário a quantidade do produto e armazena como um número inteiro (int)

totalsemdesconto = valor_unitario * quantidade  # Calcula o valor total sem desconto multiplicando o valor unitário pela quantidade

if quantidade <= 9:  # Verifica se a quantidade é menor ou igual a 9
    desc = 0  # Define o desconto como 0, ou seja, sem desconto
    printdesc = 0
elif quantidade <= 99:  # Verifica se a quantidade é menor ou igual a 99
    desc = 0.05  # Define o desconto como 0.05, ou seja, 5%
    printdesc = 5
elif quantidade <= 999:  # Verifica se a quantidade é menor ou igual a 999
    desc = 0.1  # Define o desconto como 0.1, ou seja, 10%
    printdesc = 10
else:  # Caso a quantidade seja maior que 999
    desc = 0.15  # Define o desconto como 0.15, ou seja, 15%
    printdesc = 15

comdesconto = totalsemdesconto - (totalsemdesconto * desc)  # Calcula o valor total com desconto subtraindo o desconto do valor total sem desconto

print("Valor total sem desconto: R$", totalsemdesconto)  # Exibe o valor total sem desconto na tela, precedido por "Valor total sem desconto: R$"
print("Valor total com desconto: R$", comdesconto, "( desconto", printdesc,"% )")  # Exibe o valor total com desconto na tela, precedido por "Valor total com desconto: R$"

print("")
print("")
