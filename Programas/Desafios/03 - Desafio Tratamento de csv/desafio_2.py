import csv
from urllib import request 
'''
Usamos o Request para fazer o download de algum arquivo.
'''

def read(url):
    with request.urlopen(url) as entrada:
        '''
        Fazemos o request do csv.
        '''
        print('Baixando Arquivos CSV ...')
        dados = entrada.read().decode('latin1')# Fazemos a leitura e decoficamos o arquivo... 
        print('Download Completo!!!')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]} : {cidade[3]}')

    if entrada.close:
        print('Arquivo fechado com sucesso')
        
if __name__ == "__main__":

    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
