# Exibição de linhas em branco
print("")
print("")
print("Lanchonete do Johnata Suzarte Souza (RU:3996609)")
print("")
# Dicionário contendo o cardápio
cardapio = {
    100: {"Descrição": "Cachorro-quente", "Valor": 9.00},
    101: {"Descrição": "Cachorro-quente Duplo", "Valor": 11.00},
    102: {"Descrição": "X-Egg", "Valor": 12.00},
    103: {"Descrição": "X-Salada", "Valor": 13.00},
    104: {"Descrição": "X-Bacon", "Valor": 14.00},
    105: {"Descrição": "X-Tudo", "Valor": 17.00},
    200: {"Descrição": "Refrigerante Lata", "Valor": 5.00},
    201: {"Descrição": "Chá Gelado", "Valor": 4.00}
}

# Exibição do cardápio
print("------ Cardápio ------")
for codigo, produto in cardapio.items():
    descricao = produto["Descrição"]
    valor = produto["Valor"]
    print(f"Código: {codigo} - Descrição: {descricao} - Valor: R${valor:.2f}")
print("----------------------")

# Dicionário para armazenar o pedido do cliente
pedido = {}
total = 0.0

# Loop para solicitar os pedidos ao cliente
while True:
    # Solicitação do código do produto ao cliente
    codigo = int(input("Digite o código do produto desejado (ou 0 para encerrar o pedido): "))
    
    if codigo == 0:
        break
    
    # Verifica se o código é válido
    if codigo not in cardapio:
        print("Opção inválida!")
        continue
    
    # Adiciona o produto ao pedido
    if codigo in pedido:
        pedido[codigo] += 1
    else:
        pedido[codigo] = 1
    
    # Exibe a confirmação do produto adicionado ao pedido
    print(f"{cardapio[codigo]['Descrição']} adicionado ao pedido.")
    
    # Loop para verificar se o cliente deseja pedir mais itens
    while True:
        mais = input("Deseja pedir mais alguma coisa? (S/N) ").upper()
        
        if mais == "S":
            break
        elif mais == "N":
            break
        else:
            print("Opção inválida!")
    
    if mais == "N":
        break

# Exibição do resumo do pedido
print("\n--- Pedido ---")

for codigo, quantidade in pedido.items():
    descricao = cardapio[codigo]["Descrição"]
    valor_unitario = cardapio[codigo]["Valor"]
    subtotal = valor_unitario * quantidade
    total += subtotal
    print(f"Código: {codigo} - Descrição: {descricao} - Quantidade: {quantidade} - Subtotal: R${subtotal:.2f}")

# Exibição do valor total do pedido
print(f"\nValor total do pedido: R${total:.2f}")
