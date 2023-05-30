import tkinter as tk

def calcular_soma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    soma = num1 + num2
    label_resultado.configure(text="Resultado: {:.2f}".format(soma))

root = tk.Tk()
root.geometry("1280x720")

label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

button_calcular = tk.Button(root, text="Calcular", command=calcular_soma)
button_calcular.pack()

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack()

caixa_vermelha = tk.Frame(root, width=1280, height=100, bg="red")
caixa_vermelha.pack(side=tk.BOTTOM)

root.mainloop()
