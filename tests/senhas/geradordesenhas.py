import pyperclip
import random
import tkinter as tk
from tkinter import *

def clique_botao():
    label.config(text="Botão Clicado!")

def randomizar():
    senharamdom = random.randint('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#')
    for i in senharamdom (0,12,1):
        senha = senha + senharamdom
    # pyperclip.copy("")

# Criar a janela principal
janela = tk.Tk()
janela.geometry("300x200")
janela.eval('tk::PlaceWindow . center')
janela.title("GERADOR DE SENHAS")
icon = tk.PhotoImage(file = 'tests/senhas/update.png ')
janela.iconphoto(True, icon)

# Criar um rótulo
label = tk.Label(janela, text="---BEM VINDO AO GERADOR DE SENHAS 2000v1---")
label.pack(padx=20,pady=30)
label.pack()

# Criar um botão
botao = tk.Button(janela, text="CLICK PARA GERAR E COPIAR", command=randomizar)
botao.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
