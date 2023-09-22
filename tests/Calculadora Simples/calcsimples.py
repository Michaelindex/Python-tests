def calculadora():
    num1 = float(input("Entre com o primeiro numero: "))
    num2 = float(input("Entre com o segundo numero: "))
    print("Escolha agora o que você quer fazer com esses 2 números informados")
    user = int(input(f"1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha: "))
    if user == 1:
        result = num1 + num2
        print(result)
        refaz()
    elif user == 2:
        result = num1 - num2
        print(result)
        refaz()
    elif user == 3:
        result = num1 * num2
        print(result)
        refaz()
    elif user == 4:
        result = num1 / num2
        print(result)
        refaz()
    else:
        print("Por favor, digite um numero entre 1 a 4.")
        calculadora()

def refaz():
    fim = input(f"Deseja recomeçar? Digite 'sim' ou 's'\nSe não só digite outra coisa: ")
    if fim == 'SIM' or 'S' or 'sim' or 's':
        calculadora()
    elif fim != 'SIM' or 'S':
        print('Thank You!!!')


calculadora()
