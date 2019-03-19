nome, idade = 'Thomas', 18
'''
Sim podemos definir 2 variaveis na mesma linha. 
fazer da seguinte maneira:
nome = 'Thomas'
idade = 18
ea mesma coisa da linha 1.
outro exemplo podemos fazer
nome, idade, sexo = 'Thomas', 18, 'Masculino'
caso você queria tirar prova disto è apenas usar print(nome) ou print(idade)
e verá que vai retornar oque foi definido.
'''

print('Nome: %s Idade: %d' % (nome,idade))
print('Nome: %s Idade: %d, %d, %d' % (nome,idade,True, False)) # imprime 0 e 1
print('Nome: %s Idade: %d, %s, %s' % (nome,idade,True, False)) # imprime True e False
'''
%s      : Referencia a uma String
%d      : Referencia um Int
%f      : Referencia um Float(Retona 6 casas padroes)
%.2f    : Referencia atè 2 casa decimais do float. (**)
%       : Para separar. 
** O numero 2 pode ser trocado por qualquer numero. ele exibira o tanto de casas decimais
definidas, no caso citado a cima seria 2 mas pode ser 3, 4, 5 oque você desejar.

note que depois da % temos entre parenteses oque iremos passar para o %s e %d. 

Esta è uma versão mais antiga, Veremos agora como fazer de uma maneira mais simples.
'''
print('Nome: {0} Idade: {1}'.format(nome,idade)) # Recomendado para python abaixo do 3.6
'''
Muito mais simples e facil desta maneira.
o nome corresponde a 0 ea idade corresponde a 1.

ainda temos uma maneira mais simples ainda de se fazer.
''' 
print(f'Nome: {nome} Idade: {idade}') # pode ou não ser usada em python 3.6 ou superior
'''
utilizamos o F na frente da aspas para referenciar o format.
e dentro dos {} nos colocamos a informação que desejamos no caso os valores
contidos dentro de nome e idade.
'''