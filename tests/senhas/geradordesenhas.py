import tkinter as tk
import tkinter

def clique_botao():
    label.config(text="Botão Clicado!")

# Criar a janela principal
janela = tk.Tk()
janela.geometry("300x200")
janela.eval('tk::PlaceWindow . center')
janela.title("Exemplo Tkinter")

# Criar um rótulo
label = tk.Label(janela, text="---BEM VINDO AO GERADOR DE SENHAS 2000v1---")
label.pack(padx=100,pady=5)#AQUI ESTA DANDO ERRO
label.pack()

# Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=clique_botao)
botao.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
