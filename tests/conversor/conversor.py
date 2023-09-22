def conversor():
    print("Aqui faremos a conversão da unidade que você escolher")
    entrada1 = int(input("Qual unidade você vai começar\n1 - mm\n2 - cm\n3 - m\n4 - km\nEscolha: "))
    entrada2 = int(input("Para qual unidade você vai converter\n1 - mm\n2 - cm\n3 - m\n4 - km\nEscolha: "))
    entrada3 = float(input("Aqui digite o valor que você deseja converter: "))
    if entrada1 == 1 and entrada2 == 2:
        resultado = entrada3 / 10
        print(f"Resultado de {entrada3}mm para cm é : {resultado:.6f}cm")
    elif entrada1 == 1 and entrada2 == 3:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}mm para m é : {resultado:.6f}m")
    elif entrada1 == 1 and entrada2 == 4:
        resultado = entrada3 / 1000000
        print(f"Resultado de {entrada3}mm para km é : {resultado:.6f}km")
    elif entrada1 == 1 and entrada2 == 1:
        print("Cara você quer saber o valor da unidade para a mesma unidada? Faz issae dnv")
        conversor()

    elif entrada1 == 2 and entrada2 == 1:
        resultado = entrada3 * 10
        print(f"Resultado de {entrada3}cm para mm é : {resultado:.6f}mm")
    elif entrada1 == 2 and entrada2 == 3:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}cm para m é : {resultado:.6f}m")
    elif entrada1 == 2 and entrada2 == 4:
        resultado = entrada3 / 1000000
        print(f"Resultado de {entrada3}cm para km é : {resultado:.6f}km")
    elif entrada1 == 2 and entrada2 == 2:
        print("Cara você quer saber o valor da unidade para a mesma unidada? Faz issae dnv")
        conversor()

    elif entrada1 == 3 and entrada2 == 1:
        resultado = entrada3 * 1000000
        print(f"Resultado de {entrada3}m para mm é : {resultado:.6f}mm")
    elif entrada1 == 3 and entrada2 == 2:
        resultado = entrada3 * 100
        print(f"Resultado de {entrada3}m para cm é : {resultado:.6f}cm")
    elif entrada1 == 3 and entrada2 == 4:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}m para km é : {resultado:.6f}km")
    elif entrada1 == 3 and entrada2 == 3:
        print("Cara você quer saber o valor da unidade para a mesma unidada? Faz issae dnv")
        conversor()

    elif entrada1 == 4 and entrada2 == 1:
        resultado = entrada3 * 1000000
        print(f"Resultado de {entrada3}km para mm é : {resultado:.6f}mm")
    elif entrada1 == 4 and entrada2 == 2:
        resultado = entrada3 * 100000
        print(f"Resultado de {entrada3}km para cm é : {resultado:.6f}cm")
    elif entrada1 == 4 and entrada2 == 3:
        resultado = entrada3 / 1000
        print(f"Resultado de {entrada3}km para m é : {resultado:.6f}m")
    elif entrada1 == 4 and entrada2 == 4:
        print("Cara você quer saber o valor da unidade para a mesma unidada? Faz issae dnv")
        conversor()

    else:
        print("Independente doq você esteja escrito isso ta errado irmão, siga os passos.")
        conversor()

conversor()