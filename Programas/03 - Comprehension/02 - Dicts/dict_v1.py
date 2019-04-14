dicionario = {i: i*2 for i in range(11) if i % 2 == 0}

print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} X 2 = {dobro}')
    '''
    Usamos a mesma logica usada para fazer o list porem agora com dicionario.
    note que imprimos a tabuada do 2 usando Dict.
    '''