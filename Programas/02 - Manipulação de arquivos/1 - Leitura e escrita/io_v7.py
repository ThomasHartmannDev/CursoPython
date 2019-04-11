
with open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8") as arquivo:
    with open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.txt',mode = 'w',encoding="utf-8") as saida:
        '''
        Abrimos o arquivo pessoas.txt em modo de escrita (mode = 'w') e demonimamos este arquivo como saida.
        '''
        for registro in arquivo: 
            pessoa = registro.strip().split(',')
            print('Nome: {} ,Idade: {}'.format(*pessoa),file = saida)
            '''
            Ao inves de printarmos no console, agora estamos printando no arquivo pessoas.txt
            '''
 

if arquivo.close:
    print('Arquivo pessoas.csv fechado com sucesso')

if saida.close:
    print('Arquivo pessoas.txt fechado com sucesso')