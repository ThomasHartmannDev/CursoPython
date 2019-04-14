generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator))# Saida 0

print(next(generator))# Saida 4

print(next(generator))# Saida 16

print(next(generator))# Saida 36

print(next(generator))# Saida 64

# print(next(generator))# ERROR
'''
O Generator ele vai "criando" os valores de acordo com a necessidade diferente
do list comprehension... o generator è ea melhor opção quando se trata de diminuir
a memoria alocada para um projeto.

como pode se ver o print(next(generator))
vai printando o proximo valor atè chegar ao seu limite.
'''


