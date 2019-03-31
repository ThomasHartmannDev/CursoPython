'''
Neste arquivo veremos um metodo diferente de leitura.

'''
arquivo = open('Programas/2 - Manipulação de arquivos/pessoas.csv',encoding="utf-8")
for registro in arquivo: # pegando direto do arquivo as informações sem salvar em uma variavel
    print('Nome: {} ,Idade: {}'.format(*registro.split(',')))
'''
Diferente do exemplo anterior que carregava todo o arquivo pra dentro da variavel
simplesmente abrimos o arquivos e carregamos apenas oque nos precisamos.
'''
arquivo.close()# Fechando o arquivo