import random
import tkinter as tk

def adivinhar_numero():
    comp = random.randint(1, 100)
    tentativas = 0

    def verificar_numero():
        nonlocal tentativas
        usr = int(entry.get())
        tentativas += 1

        if usr > comp:
            resultado_label.config(text="Um pouco menos")
        elif usr < comp:
            resultado_label.config(text="Um pouco mais")
        else:
            resultado_label.config(text=f"BOAA! Você acertou em {tentativas} tentativa(s)!")

    # Configuração da janela principal
    janela = tk.Tk()
    janela.title("Jogo de Adivinhação")
    janela.geometry("300x200")

    # Rótulo e campo de entrada
    instrucao_label = tk.Label(janela, text="Digite um número de 1 a 100:")
    instrucao_label.pack()

    entry = tk.Entry(janela)
    entry.pack()

    # Botão de envio
    enviar_button = tk.Button(janela, text="Enviar", command=verificar_numero)
    enviar_button.pack()

    # Rótulo de resultado
    resultado_label = tk.Label(janela, text="")
    resultado_label.pack()

    # Inicia a interface gráfica
    janela.mainloop()

adivinhar_numero()
