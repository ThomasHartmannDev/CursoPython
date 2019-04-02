import csv

with open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8") as entrada:
    for pessoa in csv.reader(entrada):
        '''
        Usando o modulo csv temos acesso ao csv.reader() que facilita nossa vida e não precisamos fazer uso de
        splits como nos exemplos (io_v1.py [...])
        '''
        print('Nome: {} ,Idade: {}'.format(*pessoa))
