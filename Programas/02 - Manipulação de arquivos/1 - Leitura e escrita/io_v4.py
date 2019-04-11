
try: #Tenta executar o codigo dentro dele...
    arquivo = open('Programas/2 - Manipulação de arquivos/1 - Leitura e escrita/pessoas.csv',encoding="utf-8")
    for registro in arquivo: 
        print('Nome: {} ,Idade: {}'.format(*registro.strip().split(',')))
finally: # Caso de algum erro ou termine a execução do bloco Try, finally será executado.
    print('Finally executado')
    arquivo.close()
    '''
    Caso o Try de algum erro ele passa pelo finally porem o resto do programa fora do finally não è executado.
    '''
