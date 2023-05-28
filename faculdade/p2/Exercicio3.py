def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            
            volume = altura * comprimento * largura
            
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
            peso = float(input("Digite o peso do objeto (em kg): "))
            
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
    
    while True:
        rota = input("Digite a rota do objeto (Sigla da cidade de origem seguida da cidade de destino): ").upper()
        
        if rota in rotas:
            return rotas[rota]
        else:
            print("Rota não aceita. Tente novamente.")

altura = dimensoesObjeto()
comprimento = dimensoesObjeto()
largura = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = altura * comprimento * largura * peso * rota

print(f"Valor total a ser pago: R${total:.2f}")
