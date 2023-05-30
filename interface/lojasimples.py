import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def exibir_menu_usuario():
    menu_usuario = tk.Toplevel(root)
    menu_usuario.configure(background="black")

    label_opcoes = tk.Label(menu_usuario, text="Escolha uma opção:", bg="black", fg="white")
    label_opcoes.pack()

    opcoes = [
        "1 - Lanche de Frango",
        "2 - Lanche de Bacon",
        "3 - X-Salada",
        "4 - Coca-Cola 2L",
        "5 - Suco 250ml"
    ]

    for opcao in opcoes:
        label = tk.Label(menu_usuario, text=opcao, bg="black", fg="white")
        label.pack()

def verificar_acesso():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "root" and senha == "123":
        messagebox.showinfo("Acesso Permitido", "God")
    else:
        messagebox.showerror("Acesso Negado", "Usuário ou senha incorretos")

root = tk.Tk()
root.configure(background="black")

style = ttk.Style()
style.configure(
    "Redondo.TFrame",
    background="white",
    borderwidth=0,
    relief="solid",
    padding=30
)

caixa_branca = ttk.Frame(root, width=300, height=200, style="Redondo.TFrame")
caixa_branca.pack(pady=50)

label_titulo = tk.Label(caixa_branca, text="Escolha uma opção:", bg="white")
label_titulo.pack()

button_usuario = tk.Button(caixa_branca, text="Usuário", command=exibir_menu_usuario, bd=0, relief="flat")
button_usuario.pack(pady=10)

button_adm = tk.Button(caixa_branca, text="Adm", command=verificar_acesso, bd=0, relief="flat")
button_adm.pack(pady=10)

label_usuario = tk.Label(caixa_branca, text="Usuário:", bd=0, relief="flat")
label_usuario.pack()

entry_usuario = tk.Entry(caixa_branca, bd=0, relief="flat")
entry_usuario.pack()

label_senha = tk.Label(caixa_branca, text="Senha:", bd=0, relief="flat")
label_senha.pack()

entry_senha = tk.Entry(caixa_branca, show="*", bd=0, relief="flat")
entry_senha.pack()

root.mainloop()
