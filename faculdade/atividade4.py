import time # Biblioteca de tempo

print("Olá usuário !")
time.sleep(1)

print("----------------------------------------------------------------------------")
print("Bem vindo a RRT(Richelmy Ryan Troes) software de estoque para bicicletaria") # RU: 4039661
print("----------------------------------------------------------------------------")

time.sleep(1.5)
print("Vamos ao software !!!")


# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    # Solicita ao usuário o código, nome, fabricante e valor da peça
    codigo = input("Digite o código da peça: ")
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))
    
    # Cria um dicionário com os dados da peça
    peca = {
        "Código": codigo,
        "Nome": nome,
        "Fabricante": fabricante,
        "Valor": valor
    }

    return peca

# Função para consultar peças
def consultarPeca(pecas):
    while True:
        print("\nMenu de Consulta de Peças:")
        print("1) Consultar Todas as Peças")
        print("2) Consultar Peças por Código")
        print("3) Consultar Peças por Fabricante")
        print("4) Retornar")

        # Solicita ao usuário uma opção de consulta
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Exibe todas as peças cadastradas
            print("\nTodas as Peças:")
            for peca in pecas :
                print(peca)
        elif opcao == "2":
            # Solicita ao usuário o código da peça a ser consultada
            codigo = input("\nDigite o código da peça: ")
            # Busca a peça pelo código e exibe os dados se encontrada
            for peca in pecas:
                if peca["Código"] == codigo:
                    print("\nPeça encontrada:")
                    print(peca)
                    break
            else:
                print("\nPeça não encontrada.")
        elif opcao == "3":
            # Solicita ao usuário o fabricante a ser consultado
            fabricante = input("\nDigite o fabricante: ")
            # Exibe todas as peças do fabricante especificado
            print("\nPeças do fabricante", fabricante + ":")
            for peca in pecas:
                if peca["Fabricante"] == fabricante:
                    print(peca)
        elif opcao == "4":
            break
        else:
            print("\nOpção inválida. Digite novamente.")

# Função para remover uma peça
def removerPeca(pecas):
    # Solicita ao usuário o código da peça a ser removida
    codigo = input("Digite o código da peça que deseja remover: ")
    # Remove a peça da lista de peças se encontrada
    for peca in pecas:
        if peca["Código"] == codigo:
            pecas.remove(peca)
            print("Peça removida com sucesso.")
            break
    else:
        print("Peça não encontrada.")

# Função principal
def main():
    pecas = []  # Lista para armazenar as peças cadastradas
    codigo = 1  # Variável para gerar o código único das peças

    while True:
        print("\nMenu Principal:")
        print("1) Cadastrar Peça")
        print("2) Consultar Peça")
        print("3) Remover Peça")
        print("4) Sair")

        # Solicita ao usuário uma opção do menu principal
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Chama a função para cadastrar uma nova peça
            peca = cadastrarPeca(codigo)

            # Adiciona a peça à lista de peças e atualiza o código
            pecas.append(peca)
            codigo += 1
            print("\nPeça cadastrada com sucesso.")
        elif opcao == "2":
            # Chama a função para consultar peças
            consultarPeca(pecas)
        elif opcao == "3":
            # Chama a função para remover uma peça
            removerPeca(pecas)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("\nOpção inválida. Digite novamente.")

# Execução do programa
main()
