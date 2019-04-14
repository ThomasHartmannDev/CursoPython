generator = (i ** 2 for i in range(10) if i % 2 == 0)


for numero in generator:
    print(numero)

'''
Usando o for não temos problema com limite ja que quando ele atinge o limite
o não gera erro difirente da versão 1 que estavamos printando e quando passava do limite
causava erro.
'''