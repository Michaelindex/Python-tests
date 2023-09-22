def conversor():
    print("Aqui faremos a conversão da unidade que você escolher")
    entrada1 = int(input("Qual unidade você vai começar\n1 - mm\n2 - cm\n3 - m\n4 - km\nEscolha: "))
    entrada2 = int(input("Para qual unidade você vai converter\n1 - mm\n2 - cm\n3 - m\n4 - km\nEscolha: "))
    entrada3 = float(input("Aqui digite o valor que você deseja converter: "))
    if entrada1 == 1 and entrada2 == 2:
        resultado = entrada3 / 10
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 1 and entrada2 == 3:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 1 and entrada2 == 4:
        resultado = entrada3 / 1000000
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 2 and entrada2 == 1:
        resultado = entrada3 * 10
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 2 and entrada2 == 3:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 2 and entrada2 == 4:
        resultado = entrada3 / 1000000
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
    elif entrada1 == 3 and entrada2 == 1:
        resultado = entrada3 * 1000000
        print(f"Resultado de {entrada3}mm para cm é : {resultado}")
