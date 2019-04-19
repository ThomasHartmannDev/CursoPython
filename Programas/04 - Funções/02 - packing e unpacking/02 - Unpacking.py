'''
Como visto no exemplo anterior de Packing onde ele gera uma tupla e faz a soma,
neste caso iremos gerar uma tupla e realizar a soma desta tupla.
'''
#Exemplo simples de soma.
# Tupla_simples = (1,2,3)
def Soma_3n(a,b,c):
    soma = a + b + c
    return soma

def soma_infinita(*numeros):
    soma = 0
    for n in numeros:
        soma += n 
    return soma


if __name__ == "__main__":
    Tupla_simples = (1,2,3)
    print(Soma_3n(*Tupla_simples))#Note que usamos o * para passar a tupla para dentro da função
    # Tenha em mente que a função de Soma_3n pega apenas 3 numero caso use uma tupla 
    # com 4 numeros ou mais vai gerar um erro.
    Lista_simples = [1,2,7]
    print(Soma_3n(*Lista_simples))# Funciona de maneira identica a tupla.


    Tupla_Grande = (1,2,3,4,5,6,7,8,10)
    print(soma_infinita(*Tupla_Grande))
    # Note que mesmo a função recebendo ja um parametro com *(tupla) temos
    # que passar o * em Tupla_grande.5
    Lista_Grande = [1,2,3,4,5,6,7,8,10,20]
    print(soma_infinita(*Lista_Grande)) #Podemos fazer o mesmo com listas.
    '''
    Neste exemplo Estamos realizando o Unpacking ou seja estamos Estraindo os valores de uma tupla e de uma lista.
    '''

