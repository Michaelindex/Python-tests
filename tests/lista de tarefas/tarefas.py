import sqlite3#CHATGPT

#Conectar ao banco de dados ( ou criar um novo )#CHATGPT
conn = sqlite3.connect('TAREFAS.db')#CHATGPT

#Criar uma tabela #CHATGPT
cursor = conn.cursor()#CHATGPT
cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, titulo TEXT, corpo TEXT)')#CHATGPT

#Consultar dados #CHATGPT
def consulta():
    cursor.execute('SELECT * FROM tarefas') #CHATGPT
    for row in cursor.fetchall(): #CHATGPT
        print(row) #CHATGPT

#Inserir dados #CHATGPT
def adicionar():
    titulo = input("Digite o título da tarefa.")
    corpo = input("Digite o corpo da tarefa")
    cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',(titulo, corpo)) #CHATGPT

#Remover dados
def remover():
    consulta()
    removid = print("Digite o ID da tarefa que você deseja remover")
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (removid))
    app()

def app():
    print("App de Tarefas - 2023v1")
    desejo = int(input("O que você quer fazer no seu App de Tarefas?\n1 - Consultar\n2 - Adicionar\n3 - Remover\n4 - Sair"))
    if desejo == 1:
        consulta()
        app()
    elif desejo == 2:
        adicionar()
        app()
    elif desejo == 3:
        remover()
        app()
    elif desejo == 4:
        print("Tchau !")
    else:
        print("Escolha um numero entre 1 a 4")
        app()

        

conn.close() #CHATGPT


