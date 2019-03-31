'''
Diferente da lista que pode ser mudada, a Tupla è imutavel.
'''
tupla_unica = ('um',) # Caso queremos apenas um item na tupla devemos deixar essa (,) no final.

tupla_cores = ('Verde','Amarelo','Azul','Branco')# não precisamos colocar a (,) no final pois o python ja entendeu que se trata de uma tupla.

print(tupla_cores[-1])
print(tupla_cores[1])
print(tupla_cores[1:])
print(tupla_cores[:4])
# funciona igual as listas. 

print(tupla_cores.index('Amarelo')) #Mostra o index do amarelo
print(tupla_cores.count('Azul')) #Mostra quantas vezes o azul aparece na tupla.

tupla_repetida = ('Verde','Amarelo','Azul','Branco','Azul','Azul','Azul','Azul','Azul','Azul')
print(tupla_repetida.count('Azul'))# neste caso temos 7 'Azul' na tupla
#Caso não tenha oque foi pedido para contar na lista ele retorna 0

#Vamos ver quantos itens tem em cada lista. 
print(len(tupla_cores))
print(len(tupla_repetida))



