'''
Uma função recursa è uma função que chama ela mesmo dentro dela,
criando como se fosse um while ou um for.

'''

def imprimir(maximo, atual):
    #Condição de parada, maximo 980
    if atual >= maximo:
        print(maximo)
        return
    print(atual, end=', ')
    imprimir(maximo, atual + 1)

imprimir(990, 1)