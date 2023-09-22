import sqlite3#CHATGPT
import keyboard#CHATGPT

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
    app()

#Inserir dados #CHATGPT
def adicionar():
    titulo = input("Digite o título da tarefa: ")
    corpo = input("Digite o corpo da tarefa: ")
    cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)', (titulo, corpo))
    conn.commit()
    print(f"Se deseja continuar aperte qualquer coisa\nSe deseja voltar digite 'ESC'\nFaça: ")
    
    # Esperar uma entrada do teclado antes de chamar evento()#CHATGPT
    keyboard.read_event(suppress=True)#CHATGPT
    
    def evento():#CHATGPT
        event = keyboard.read_event()#CHATGPT
        if event.name == 'esc':#CHATGPT
            print("Saindo...")#CHATGPT
            app()#CHATGPT
        else:#CHATGPT
            adicionar()#CHATGPT
    
    evento()#CHATGPT
    # titulo = input("Digite o título da tarefa: ")
    # corpo = input("Digite o corpo da tarefa: ")
    # cursor.execute('INSERT INTO tarefas (titulo, corpo) VALUES (?, ?)',(titulo, corpo)) #CHATGPT
    # print(f"Se deseja continuar aperte qualquer coisa\nSe deseja voltar digite 'ESC'\nFaça: ")
    # def evento():
    #     event = keyboard.read_event()#CHATGPT
    #     if event.name == 'esc':#CHATGPT
    #         print("Saindo...")#CHATGPT
    #         app()#CHATGPT
    #     else:#CHATGPT
    #         adicionar()#CHATGPT
    # evento()
    # event = keyboard.read_event()#CHATGPT
    # if event.event_type == keyboard.KEY_DOWN:#CHATGPT
    #     if event.name == 'enter':#CHATGPT
    #         adicionar()#CHATGPT
    #     elif event.name == 'esc':#CHATGPT
    #         print("SAINDO...")#CHATGPT
    #         app()
    #     else:
    #         print("Refaça!")
    #         adicionar()

#Remover dados
def remover():
    cursor.execute('SELECT * FROM tarefas') #CHATGPT
    for row in cursor.fetchall(): #CHATGPT
        print(row) #CHATGPT
    
    # Solicitar o ID da tarefa a ser removida e garantir que seja um número inteiro válido#CHATGPT
    while True:#CHATGPT
        removid = input("Digite o ID da tarefa que você deseja remover: ")#CHATGPT
        if removid.isdigit():#CHATGPT
            removid = int(removid)#CHATGPT
            break#CHATGPT
        else:#CHATGPT
            print("Por favor, digite um número válido.")#CHATGPT

    # Verificar se o ID existe antes de executar a exclusão#CHATGPT
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (removid,))#CHATGPT
    if cursor.fetchone() is not None:#CHATGPT
        cursor.execute('DELETE FROM tarefas WHERE id = ?', (removid,))#CHATGPT
        conn.commit()#CHATGPT
        print("REMOVIDO !!!")#CHATGPT
    else:#CHATGPT
        print("ID não encontrado.")#CHATGPT

    app()#CHATGPT
    # consulta()
    # removid = input("Digite o ID da tarefa que você deseja remover")
    # cursor.execute('DELETE FROM tarefas WHERE id = ?', (removid))
    # conn.commit()
    # print("REMOVIDO !!!")
    # app()

def app():
    print("\n\n\nApp de Tarefas - 2023v1")
    desejo = int(input("O que você quer fazer no seu App de Tarefas?\n1 - Consultar\n2 - Adicionar\n3 - Remover\n4 - Sair\n"))
    if desejo == 1:
        consulta()
    elif desejo == 2:
        adicionar()
    elif desejo == 3:
        remover()
    elif desejo == 4:
        print("Tchau !")
    else:
        print("Escolha um numero entre 1 a 4")
        app()

app()

conn.close() #CHATGPT


