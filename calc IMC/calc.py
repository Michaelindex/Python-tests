# CALC SIMPLES DO IMC

#peso = float(input("Qual é seu peso"))
#altura = float(input("Qual sua altura"))
#print(peso / (altura*altura))


def imc (peso, altura):
    return (peso / (altura * altura))

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

print(imc(peso, altura))




