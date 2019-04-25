def executar(funcao):
    if callable(funcao): #Fazemos a verificação se oque foi passado como parametro è uma função ou não
        return funcao()
    else: 
        return print('Isso não è uma função, tente usar: \n executar(bom_dia) \n executar(boa_tarde)')
'''
A função executar ela esta "invocando" uma função neste caso ela invoca
oque foi passado como parametro para ela.
'''

def bom_dia():
    print('Bom dia')

def boa_tarde():
    print('Boa Tarde')


if __name__ == "__main__":
    '''
    Passamos como parametro uma função de bom dia e boa tarde para ser executada apartir de uma
    terceira função no caso a função executar
    '''
    executar(bom_dia)

    executar(boa_tarde)

    executar(1)
'''
Porque não chamar a função de maneira direta ?
a resposta è simples dentro da função executar nos podemos fazer verificações por exemplo e 
tornar nosso codigo mais seguro por exemplo

'''
