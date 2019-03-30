'''
Fizemos uso do mesmo SUM() para somar todos os valores imprimidos na lista.
''' 

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])


    return resultado

if __name__ == "__main__":

    for fib in fibonacci(10000):
        print(fib, end=', ')

    print('\nSoma de total è : ',sum(fibonacci(10000)))