import time #Biblioteca de tempo
print("Olá usuário !")
time.sleep(1) #Espera de 1s
print("----------------------------------------")
print("Bem vindo a loja do Richelmy Ryan Troes") #RU: 4039661
print("----------------------------------------")
time.sleep(1.5) #Espera de 1.5s
print("Vamos as compras !!!")

def calcular_desconto(valor_unitario, quantidade): #Para facilitar criei uma função para calcular o desconto usando o if elif else
    
    valor_total_sem_desconto = valor_unitario * quantidade #Processamento
    if quantidade <= 9:                                    #Processamento
        desconto = 0                                       #Processamento
    elif quantidade <= 99:                                 #Processamento         
        desconto = 0.05                                    #Processamento   Logo a cima ele faz o calc. bem simples e o jogo de if elif else abaixo
    elif quantidade <= 999:                                #Processamento
        desconto = 0.1                                     #Processamento 
    else:                                                  #Processamento
        desconto = 0.15                                    #Processamento

    valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * desconto) #Processamento

    return valor_total_sem_desconto, valor_total_com_desconto

valor_unitario = float(input("Digite o valor unitário do produto: ")) #Perguntar ao usuário o Valor
quantidade = int(input("Digite a quantidade do produto: ")) #Perguntar ao usuário a quantidade

total_sem_desconto, total_com_desconto = calcular_desconto(valor_unitario, quantidade)# Cálculo dos valores com desconto

print("Valor total sem desconto: R$", total_sem_desconto) #Imprimir na tela o total sem desconto
print("Valor total com desconto: R$", total_com_desconto) #Imprimir na tela o total com desconto
