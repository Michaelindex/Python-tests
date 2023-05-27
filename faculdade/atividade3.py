import time # Biblioteca de tempo

print("Olá usuário !")
time.sleep(1)

print("--------------------------------------------------------")
print("Bem vindo a empresa de Logística do Richelmy Ryan Troes") # RU: 4039661
print("--------------------------------------------------------")
time.sleep(1.5)
print("Vamos aos preços !!!")

def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): ")) # Pergunta a altura do objeto
            comprimento = float(input("Digite o comprimento do objeto (em cm): ")) # Pergunta o comprimento do objeto
            largura = float(input("Digite a largura do objeto (em cm): ")) # Pergunta a largura do objeto

            volume = altura * comprimento * largura # Calcula o volume do objeto

            if volume < 1000:
                print("O volume do objeto é : ", volume)
                return 10 # Retorna o valor correspondente às dimensões do objeto
            elif 1000 <= volume < 10000:
                print("O volume do objeto é : ", volume)
                return 20
            elif 10000 <= volume < 30000:
                print("O volume do objeto é : ", volume)
                return 30
            elif 30000 <= volume < 100000:
                print("O volume do objeto é : ", volume)
                return 50
            else:
                print(f"O volume do objeto é: {volume}")
                print("Não aceitamos objetos com dimensões tão grandes.") # Se as dimensões não estiverem dentro dos limites aceitos, imprime uma mensagem de erro
        except ValueError:
            print("Valor inválido. Digite novamente.") # Se um valor não numérico for digitado, imprime uma mensagem de erro
dimensoes = dimensoesObjeto()
print("")
print("")

def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): ")) # Pergunta o peso do objeto

            if peso <= 0.1:
                return 1 # Retorna o valor correspondente ao peso do objeto
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print("Não aceitamos objetos tão pesados. Digite novamente por favor.") # Se o peso não estiver dentro dos limites aceitos, imprime uma mensagem de erro
        except ValueError:
            print("Você digitou peso do objeto com valor não numérico") # Se um valor não numérico for digitado, imprime uma mensagem de erro
peso = pesoObjeto()

print("")
def rotaObjeto():
    while True:
        print("")   
        print("Segue abaixo as seguintes rotas.")
        print("RS - De Rio de Janeiro até São Paulo")
        print("SR - De São Paulo até Rio de Janeiro")
        print("BS - De Brasília até São Paulo")
        print("SB - De São Paulo até Brasília")
        print("BR - De Brasília até Rio de Janeiro")
        print("RB - Rio de Janeiro até Brasília")

        rota = input("Digite a rota do objeto: ") # Pergunta a rota desejada para o objeto

        if rota == "RS":
            return 1 # Retorna o valor correspondente à rota escolhida
        elif rota == "SR":
            return 1
        elif rota == "BS":
            return 1.2
        elif rota == "SB":
            return 1.2
        elif rota == "BR":
            return 1.5
        elif rota == "RB":
            return 1.5
        else:
            print("Rota inválida. Digite novamente.") # Se uma rota inválida for digitada, imprime uma mensagem de erro
rota = rotaObjeto()
print("")
print("")

total = dimensoes * peso * rota # Calcula o valor total a ser pago

print(f"Total a ser pago: R${total:.2f} ( dimensões:", dimensoes, "* peso:", peso, "* rota:", rota, ")") # Imprime o total a ser pago formatado com 2 casas decimais
