def calcular_desconto(valor_unitario, quantidade):
    valor_total_sem_desconto = valor_unitario * quantidade

    if quantidade <= 9:
        desconto = 0
    elif quantidade <= 99:
        desconto = 0.05
    elif quantidade <= 999:
        desconto = 0.1
    else:
        desconto = 0.15

    valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * desconto)

    return valor_total_sem_desconto, valor_total_com_desconto

# Entrada de dados
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo dos valores com desconto
total_sem_desconto, total_com_desconto = calcular_desconto(valor_unitario, quantidade)

# Saída do código
print("Valor total sem desconto: R$", total_sem_desconto)
print("Valor total com desconto: R$", total_com_desconto)
