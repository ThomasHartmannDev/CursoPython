'''
Agora passamos a definir o tamanho da lista, por exemplo 20 numeros.
quando a lista atinge 20 numeros dentro dela è chamado o BREAK que encerra o while.

''' 

def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break

    return resultado

if __name__ == "__main__":
    quantidade = 21 # Quantidade de numeros presente dentro da lista.
    for fib in fibonacci(quantidade):
        print(fib, end=', ')

    print('\nSoma de total è : ',sum(fibonacci(quantidade)))