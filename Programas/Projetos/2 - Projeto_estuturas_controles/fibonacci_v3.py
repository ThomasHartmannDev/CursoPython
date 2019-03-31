'''
Nesta terceira versão iremos fazer o swap de variaveis.
'''
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=', ')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=', ')

if __name__ == "__main__":

    fibonacci(10000)