import tkinter as tk
from tkinter import *
import tkinter

def clique_botao():
    label.config(text="Botão Clicado!")

# Criar a janela principal
janela = tk.Tk()
janela.geometry("300x200")
janela.eval('tk::PlaceWindow . center')
janela.title("GERADOR DE SENHAS")
icon = tk.PhotoImage(file = 'tests/senhas/github.png ')
janela.iconphoto(True, icon)

# Criar um rótulo
label = tk.Label(janela, text="---BEM VINDO AO GERADOR DE SENHAS 2000v1---")
label.pack(padx=20,pady=50)#AQUI ESTA DANDO ERRO
label.pack()

# Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=clique_botao)
botao.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
