def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Altura do objeto em cm: "))  # Solicita a altura do objeto ao usuário
            comprimento = float(input("Comprimento do objeto em cm: "))  # Solicita o comprimento do objeto ao usuário
            largura = float(input("Largura do objeto em cm: "))  # Solicita a largura do objeto ao usuário
            
            volume = altura * comprimento * largura  # Calcula o volume do objeto
            
            # Define o valor com base no volume do objeto
            if volume < 1000:
                return 10
            elif 1000 <= volume < 10000:
                return 20
            elif 10000 <= volume < 30000:
                return 30
            elif 30000 <= volume < 100000:
                return 50
            else:
                print("Volume não aceito. Tente novamente.")
        except ValueError:
            print("Valor não numérico. Tente novamente.")

def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))  # Solicita o peso do objeto ao usuário
            
            # Define o multiplicador com base no peso do objeto
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print("Peso não aceito. Tente novamente.")
        except ValueError:
            print("Valor não numérico. Tente novamente.")

def rotaObjeto():
    rotas = {
        "RS": 1,
        "SR": 1,
        "BS": 1.2,
        "SB": 1.2,
        "BR": 1.5,
        "RB": 1.5
    }
    
    print("Rotas disponíveis:")  # Exibe as rotas disponíveis para o usuário
    for rota, multiplicador in rotas.items():
        print(f"{rota}: {multiplicador}")
    
    while True:
        rota = input("Digite a rota do objeto (Sigla da cidade de origem seguida da cidade de destino): ").upper()  # Solicita a rota do objeto ao usuário
        
        if rota in rotas:
            return rotas[rota]  # Retorna o multiplicador correspondente à rota escolhida
        else:
            print("Rota não aceita. Tente novamente.")

altura = dimensoesObjeto()  # Obtém a dimensão do objeto (valor correspondente ao volume)
peso = pesoObjeto()  # Obtém o peso do objeto (valor correspondente ao multiplicador)
rota = rotaObjeto()  # Obtém a rota do objeto (valor correspondente ao multiplicador)

total = altura * peso * rota  # Calcula o valor total a ser pago

print(f"Valor total a ser pago: R${total:.2f}")  # Exibe o valor total a ser pago
