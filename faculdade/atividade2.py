import time #Biblioteca de tempo
print("Olá usuário !")
time.sleep(1.5) #Espera de 1s
print("-----------------------------------------------")
print("Bem vindo a lanchonete do Richelmy Ryan Troes") #RU: 4039661
print("-----------------------------------------------")
time.sleep(2.5) #Espera de 1.5s
print("Segue cardapio para compras")
time.sleep(2)

cardapio = { # Tabela de produtos
    100: {"descricao": "Cachorro-quente", "valor": 9.00},
    101: {"descricao": "Cachorro-quente Duplo", "valor": 11.00},
    102: {"descricao": "X-Egg", "valor": 12.00},
    103: {"descricao": "X-Salada", "valor": 13.00},
    104: {"descricao": "X-Bacon", "valor": 14.00},
    105: {"descricao": "X-Tudo", "valor": 17.00},
    200: {"descricao": "Refrigerante Lata", "valor": 5.00},
    201: {"descricao": "Chá Gelado", "valor": 4.00}
}

print("CARDÁPIO\n") #contra barra N para quebrar a linha
print("{:<8} {:<20} {:<8}".format("CÓDIGO", "DESCRIÇÃO", "VALOR")) #Imprimir CODIGO DESCRICAO VALOR

for codigo, produto in cardapio.items(): #Criado um for para facilitar imprimir o cardapio
    descricao = produto["descricao"]
    valor = produto["valor"]
    print("{:<8} {:<20} R${:<8.2f}".format(codigo, descricao, valor)) #Imprimir os valores

print()

total_conta = 0.0 # Inicialização das variáveis

while True: #ficar infinitamente repetindo
    codigo = int(input("Digite o código do produto desejado: ")) # Entrada do código do produto

    if codigo in cardapio: # Verifica se o código existe no cardápio
        produto = cardapio[codigo]
        total_conta += produto["valor"]
        print(f"Produto adicionado: {produto['descricao']} - Valor: R${produto['valor']:.2f}")
    else:
        print("Opção inválida!")

    resposta = input("Deseja pedir mais alguma coisa? (S/N): ") # Pergunta se o cliente deseja pedir mais algo

    if resposta.upper() == "N": #AQUI VALIDANDO SE O CLIENTE QUER (S) OU NÃO QUER (N) CONTINUAR COMPRANDO
        break
    elif resposta.upper() != "S":
        print("Opção inválida!")
        continue

print(f"\nTotal da conta: R${total_conta:.2f}") # Encerramento da conta do cliente
