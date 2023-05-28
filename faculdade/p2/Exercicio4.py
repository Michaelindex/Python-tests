print("")
print("")
print("Aplicativo de bicicletaria feito por Johnata Suzarte Souza (RU:3996609)")
print("")
def cadastrarPeca(codigo):
    codigo = (input("Código da peça: "))  # Solicita o código da peça ao usuário
    nome = input("Nome da peça: ")  # Solicita o nome da peça ao usuário
    fabricante = input("Fabricante da peça: ")  # Solicita o fabricante da peça ao usuário
    valor = float(input("Valor da peça: "))  # Solicita o valor da peça ao usuário

    peca = {
        "Código": codigo,
        "Nome": nome,
        "Fabricante": fabricante,
        "Valor": valor
    }
    return peca

def consultarPeca(pecas):
    while True:
        print("Menu de Consulta:")
        print("1) Consultar Todas as Peças cadastradas")  # Opção para consultar todas as peças cadastradas
        print("2) Consultar as Peças por Código")  # Opção para consultar peças por código
        print("3) Consultar as Peças por Fabricante")  # Opção para consultar peças por fabricante
        print("4) Retornar ao menu anterior")  # Opção para retornar ao menu principal
        
        opcao = input("Digite uma opção: ")  # Solicita ao usuário que digite uma opção do menu

        if opcao == "1":
            print("Peças que foram cadastradas:")
            for peca in pecas:
                print("----------------------------------------")
                print("Código:", peca["Código"])  # Exibe o código da peça
                print("Nome:", peca["Nome"])  # Exibe o nome da peça
                print("Fabricante:", peca["Fabricante"])  # Exibe o fabricante da peça
                print("Valor:", peca["Valor"])  # Exibe o valor da peça
                print("----------------------------------------")
        elif opcao == "2":
            codigo = input("Digite o código da peça: ")  # Solicita ao usuário que digite o código da peça
            peca = buscarPecaPorCodigo(pecas, codigo)
            if peca:
                print("Peça encontrada:")
                print("----------------------------------------")
                print("Código:", peca["Código"])  # Exibe o código da peça encontrada
                print("Nome:", peca["Nome"])  # Exibe o nome da peça encontrada
                print("Fabricante:", peca["Fabricante"])  # Exibe o fabricante da peça encontrada
                print("Valor:", peca["Valor"])  # Exibe o valor da peça encontrada
                print("----------------------------------------")
            else:
                print("Peça não encontrada.")
        elif opcao == "3":
            fabricante = input("Digite o fabricante da peça: ")  # Solicita ao usuário que digite o fabricante da peça
            pecas_fabricante = buscarPecasPorFabricante(pecas, fabricante)
            if pecas_fabricante:
                print("Peças encontradas:")
                for peca in pecas_fabricante:
                    print("----------------------------------------")
                    print("Código:", peca["Código"])  # Exibe o código da peça encontrada
                    print("Nome:", peca["Nome"])  # Exibe o nome da peça encontrada
                    print("Fabricante:", peca["Fabricante"])  # Exibe o fabricante da peça encontrada
                    print("Valor:", peca["Valor"])  # Exibe o valor da peça encontrada
                    print("----------------------------------------")
            else:
                print("Nenhuma peça encontrada para o fabricante especificado.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def buscarPecaPorCodigo(pecas, codigo):
    for peca in pecas:
        if peca["Código"] == codigo:  # Verifica se o código da peça corresponde ao código fornecido
            return peca
    return None

def buscarPecasPorFabricante(pecas, fabricante):
    pecas_fabricante = []
    for peca in pecas:
        if peca["Fabricante"] == fabricante:  # Verifica se o fabricante da peça corresponde ao fabricante fornecido
            pecas_fabricante.append(peca)
    return pecas_fabricante

def removerPeca(pecas):
    codigo = input("Digite o código da peça a ser removida: ")  # Solicita ao usuário que digite o código da peça a ser removida
    peca = buscarPecaPorCodigo(pecas, codigo)
    if peca:
        pecas.remove(peca)  # Remove a peça da lista de peças
        print("Peça removida com sucesso.")
    else:
        print("Peça não encontrada.")

pecas = []

while True:
    print("Menu:")
    print("1. Cadastrar Peça")  # Opção para cadastrar uma nova peça
    print("2. Consultar Peça")  # Opção para consultar peças cadastradas
    print("3. Remover Peça")  # Opção para remover uma peça cadastrada
    print("4. Sair")  # Opção para sair do programa
    
    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu
    
    if opcao == "1":
        codigo = len(pecas) + 1
        peca = cadastrarPeca(codigo)
        pecas.append(peca)  # Adiciona a nova peça à lista de peças
        print("Peça cadastrada com sucesso.")
    elif opcao == "2":
        consultarPeca(pecas)
    elif opcao == "3":
        removerPeca(pecas)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
