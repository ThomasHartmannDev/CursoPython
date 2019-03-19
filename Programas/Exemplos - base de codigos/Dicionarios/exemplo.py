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

#Vai ter continuação neste mesmo arquivo.