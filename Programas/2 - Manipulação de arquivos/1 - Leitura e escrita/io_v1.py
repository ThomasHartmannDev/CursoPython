'''
Neste Arquivos vamos fazer a leitura do pessoas.csv
'''


arquivo = open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8") #Estamos abrindo o arquivo pessoas.csv
'''
Vale lembrar que dentro dos () do open deve se passar o caminho do arquivo,
como o arquivo pessoas.csv esta na mesma pasta apenas colocamos pessoas.csv

tambem deve se passar o parametro encoding="utf-8" para não ter problemas de acentuação.
'''

dados = arquivo.read() #Estamos Lendo o arquivo e armazenando dentro da variavel dados

arquivo.close() # Fechamos o arquivo para não ficar aberto gastando recursos

for registro in dados.splitlines(): #Faremos um for e usando splitlines() dividiremos em linhas. 
    print('Nome: {} ,Idade: {}'.format(*registro.split(','))) #usando Split(',') Fazemos a divisão pela virgula.
    

# Veja a proxima versão
