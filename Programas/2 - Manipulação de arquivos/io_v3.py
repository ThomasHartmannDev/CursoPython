

arquivo = open('Programas/2 - Manipulação de arquivos/pessoas.csv',encoding="utf-8")
for registro in arquivo: 
    print('Nome: {} ,Idade: {}'.format(*registro.strip().split(',')))
    #Adicionamos o STRIP para retirar linhas em branco

arquivo.close()