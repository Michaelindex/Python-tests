
print("Loja do Johnata suzarte souza (RU:3996609)")

valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

totalsemdesconto = valor_unitario * quantidade

if quantidade <= 9:
    desc = 0
elif quantidade <= 99:
    desc = 0.05
elif quantidade <= 999:
    desc = 0.1
else:
    desc = 0.15

comdesconto = totalsemdesconto - (totalsemdesconto * desc)

print("Valor total sem desconto: R$", totalsemdesconto)
print("Valor total com desconto: R$", comdesconto)
