import tkinter as tk

def obter_dados():
    valor = entry.get()
    print("Valor inserido:", valor)

root = tk.Tk()

label = tk.Label(root, text="Digite um valor:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Obter Dados", command=obter_dados)
button.pack()

root.mainloop()
