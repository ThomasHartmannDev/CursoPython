'''
Substituimos o While por um for com um Range. 
''' 

def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2,quantidade): #ele tera a range desde os 2 itens ja presente na lista atè o limite, a quantidade definida
        resultado.append(sum(resultado[-2:]))

    return resultado

if __name__ == "__main__":
    quantidade = 20 # Quantidade de numeros presente dentro da lista.
    for fib in fibonacci(quantidade):
        print(fib, end=' ')

    print('\nSoma de total è : ',sum(fibonacci(quantidade)))