
try: #Tenta executar o codigo dentro dele...
    arquivo = open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8")
    for registro in arquivo: 
        print('Nome: {} ,Idade: {}'.format(*registro.strip().split(',')))

except IndexError: # o except apenas entra em ação caso de algum erro no try.
    pass
    '''
    o except permite que o resto do codigo seja executado e não parado
    '''
finally: # Caso de algum erro ou termine a execução do bloco Try, finally será executado.
    print('Finally executado')
    arquivo.close()

if arquivo.close:
    print('Arquivo fechado com sucesso')