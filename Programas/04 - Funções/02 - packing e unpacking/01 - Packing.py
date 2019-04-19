

# Uma função de soma simples como exemplo 2 + 2 pode ser limitada (como o exemplo a baixo) 
# caso queira somar varios numeros

def soma_2(a,b):
    return a + b

'''
``Ah mas eu quero fazer a soma de 10 numeros`` 

exatamente ficar criando a b c d e, atè chegar na quantidade desejada è
meio exagerado não acha ?
então podemos fazer o uso do (* - Asterisco, asteristico como vc preferir chamar isso).
o * ele faz com que nos possamos criar uma tupla e fazermos oque bem entendermos com ela.
'''
def soma_infinita(*numeros): # com *numeros, podemos colocar quantos numeros nos quisermos.
    soma = 0
    for n in numeros: #Realizamos um FOR para realizat a soma dos numeros.
        soma += n 
    return soma

if __name__ == "__main__":
    print(soma_infinita(1))
    print(soma_infinita(1,2))
    print(soma_infinita(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

# Note que podemos passar desde apenas 1 valor ou varios como 
# na linha 26 que passamos 20 valores diferentes.

