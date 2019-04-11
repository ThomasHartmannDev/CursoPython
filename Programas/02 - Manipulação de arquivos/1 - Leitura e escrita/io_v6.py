
with open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8") as arquivo:
    '''
    O bloco With garante que o arquivo aberto seja fechado no final da execução

    porem caso ocorra algum erro não è fechado o codigo para onde deu erro.s
    '''
    for registro in arquivo: 
        print('Nome: {} ,Idade: {}'.format(*registro.strip().split(',')))
 

if arquivo.close:
    print('Arquivo fechado com sucesso')