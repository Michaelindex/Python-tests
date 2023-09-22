import sqlite3#CHATGPT

#Conectar ao banco de dados ( ou criar um novo )#CHATGPT
conn = sqlite3.connect('TAREFAS.db')#CHATGPT

#Criar uma tabela #CHATGPT
cursor = conn.cursor()#CHATGPT
cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, titulo TEXT, corpo TEXT)')#CHATGPT

#Inserir dados #CHATGPT
cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',('Estudos', 'Preciso estudar Python')) #CHATGPT
cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',('Estudos', 'Preciso estudar JavaScript')) #CHATGPT
cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',('Trabalho', 'Preciso estudar Pfsense')) #CHATGPT
cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',('Trabalho', 'Preciso criar o desenho da Infra')) #CHATGPT

#Consultar dados #CHATGPT
cursor.execute('SELECT * FROM tarefas') #CHATGPT
for row in cursor.fetchall(): #CHATGPT
    print(row) #CHATGPT

conn.close() #CHATGPT


# print("-----LISTANDO SUAS TAREFAS-----")
# def tarefas():
#     escolha = int(input("Digite o que você deseja fazer\n1 - Consultar tarefas\n2 - Adicionar tarefas\n3 - Remover tarefas"))
