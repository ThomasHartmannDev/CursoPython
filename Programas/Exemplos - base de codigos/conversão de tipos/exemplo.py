# print(2 + 2) funciona normal, soma 

# print(2 + '2') não ira funcionar desse jeito.
print('=_=_=_=_=_=_=_=_=_ Conversão de tipos do py =_=_=_=_=_=_=_=_=_')

a = 2 
b = '3'
c = 2.3

print(type(a))
print(type(b))
print(type(c))

print(a + int(b))
'''
Como podemos ver nas linha 9, a variavel B è do tipo str(String)
desde jeito nos transformamos a variavel B em Int(Inteiro), mesmo
tipo da variavel A. 
'''
print(str(a) + b)

'''
Mesma coisa que no comentario acima, a diferença que transformamos a variavel A em Str,
diferente da linha 11 neste caso não irá somar mas sim concatenar ou seja juntar 2 ao lado de 3
resultando 23.
'''

#print(2 + int('2 oi tudo bem ?'))
'''
a linha 25 não pode ser feita de forma alguma.
o python não transforma literal em numeros apenas numeros.
caso seja apenas um '2' não tera problema algum.
'''
#print(a + int('3.4'))
'''
A linha 31 correra erro pois não se trata de um INT e sim de um float.
'''
print(a +float('3.4'))

# Conversão automatica feita pelo py.

print('=_=_=_=_=_=_=_=_=_ Conversão automatica do py =_=_=_=_=_=_=_=_=_')
a = 10/2
print(a)
print(type(a))

b = 10//3
print(b)
print(type(b))

c = 10 / 3
print(c)
print(type(c))

d = 10 / 2.5
print(d)
print(type(d))

e = 10 // 2.5
print(e)
print(type(e))
'''
Note que mesmo 'D' e 'E' sendo valores resultados em 4 o python interpreta como 4.0 sendo assim um float

'''
print("-.-.-.-.-.-.-.")
print(2 + True) # True è valido como 1 
print(2 + False) # False è valido como 0 
'''
Note que conseguimos somar ou subtrair True e False com algum numero.
ja que o python atrui valores 1 e 0 para os mesmos

''' 
