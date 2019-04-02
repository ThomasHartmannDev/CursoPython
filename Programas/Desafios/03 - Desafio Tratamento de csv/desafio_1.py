import csv
def desafio():
    with open('Programas/Desafios/03 - Desafio Tratamento de csv/desafio-ibge.csv', encoding='ISO-8859-1') as entrada:
        print('Lendo Arquivo...')
        dados = entrada.read()
        print('Leitura completa...')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]} : {cidade[3]}')


    if entrada.close:
        print('Arquivo fechado com sucesso')   

if __name__ == "__main__":
    desafio()