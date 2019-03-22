dicionario = {
    'Key1':'Valor1',
    'Key2':'Valor2'
}
'''
Um dicionario ou uma dict como è chamado pelo python, tabalham com chave e falor.
caso vc tenha a chava Key1, ele ira te retornar Valor1
'''
print(dicionario['Key1'])







Pessoa = {
    'Nome':'Thomas Hartmann',
    'Idade': 18,
    'Cursos':['Python basico ao avançado','Html + CSS','Alemão A1','Git e Github para iniciantes']
}
print(Pessoa)
print(Pessoa['Nome'])

print(Pessoa.keys()) # Pega todas as Keys dentro da dict.
print(Pessoa.values())# Pega todos os valores dentro da dict.
print(Pessoa.items())# Pega todos os itens dentro da dict. Exemplo de item = ('Nome':'Thomas Hartmann')

print(Pessoa.get('Idade'))# Pega a idade. caso não exista retorna None.
print(Pessoa.get('Tags',[]))# Pega Tags, caso não exista retorna uma lista vazia.
print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=')

Pessoas = {
    'Pessoa1':{
    'Nome':'Thomas Hartmann',
    'Idade': 18,
    'Cursos':['Python basico ao avançado','Html + CSS','Alemão A1','Git e Github para iniciantes']
    },
    'Pessoa2':{
    'Nome':'Daniel Santos',
    'Idade': 22,
    'Cursos':['Python basico ao avançado', 'Javascript', 'Java']  
    }
}
'''
Neste caso temos uma dict dentro de outra dict.

'''
print('-.-.-.-.- Pessoa1-.-.-.-.-.-')
# acessamos a DICT Pessoas e dentro dela usamos a Key pessoa1 e depois a Key Nome para termos acesso ao nome.
# e assim por diante para o resto das keys.
print(Pessoas['Pessoa1']['Nome'])
print(Pessoas['Pessoa1']['Cursos'])
print('-.-.-.-.- Pessoa2-.-.-.-.-.-')
print(Pessoas['Pessoa2']['Nome'])
print(Pessoas['Pessoa2']['Cursos'])

print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=')

Dict_Pessoa = {
    'Nome':'Thomas Hartmann',
    'Idade': 18,
    'Cursos':['Python']
}
print(Dict_Pessoa)
'''
Nós temos uma lista dentro de uma dict e podemos do mesmo jeito que nos modificamos a lista normalmentente
podemos modificala dentro de uma dict
''' 
Dict_Pessoa['Cursos'].append('JavaScript')
Dict_Pessoa['Cursos'].append('React')

print(Dict_Pessoa)
'''
Nos tambem podemos Retirar coisas desta lista.
'''
Dict_Pessoa['Cursos'].remove('JavaScript')
print(Dict_Pessoa)

print(Dict_Pessoa.pop('Idade'))
print(Dict_Pessoa)
'''
o Pop ele pega um valor, neste caso a idade, imprime ela no console e depois a retira de dentro da dict
note no console que a Key Idade não aparece mais na dict.
'''
Dict_Pessoa.update({'Idade':17,'Sexo':'Masculino'})
'''
Usando o .update() podemos passar KEY:VALUE pra dentro da dict.
a ordem não algo necessario pois è indexado por string e tendo a Key pode se acessar ela 
sem problema algum. 

a dict se assemelha muito ao Json.
'''
print(Dict_Pessoa)

del Dict_Pessoa['Cursos'] # Estamos deletando a lista cursos. 
print(Dict_Pessoa)
'''
Quero adicionar uma lista, para ficar no final da dict como era antes, como eu faço ? 
'''
Dict_Pessoa.update({'Cursos':['Python', 'React']})
print(Dict_Pessoa)
'''
Pronto Sua lista foi Criada e colocada no final da lista.
Note que sempre que você usar update pra adicionar algo na lista
ela será criada sempre no final da lista.
'''
Dict_Pessoa.clear() # E por final vamos limpar toda a dict e ter uma dict vazia.
'''
Vale lembrar que o mesmo funciona para Dict dentro de dict basta apenas colocar o caminho correto.
'''
print(Dict_Pessoa)