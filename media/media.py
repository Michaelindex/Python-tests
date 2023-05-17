valor = 0
nota = 0
raio = int(input("Quer calcular a media de quantas notas?: "))
for i in range (raio):
    valor = valor + nota
    nota = int(input("Me fale suas notas em sequencia: "))
print(valor)
