dicionario = {"gato": "chat", "cachorro": "dog", "peixe": "fixe"} #dicionario padrão

dicionario ['cavalo'] = 'horse' #adicionando item ao dicionario
dicionario.update({"cavalo": "horse", "pato": "ducky"}) #adiconando mais de um item ao dicinario
del dicionario['pato'] #apagando o item pato
dicionario.popitem() #apagando o ultimo item do dicionario

print(dicionario) #Mostrando tudo no dicionario

print(dicionario['cavalo']) #Mostrando apenas o item cavalo