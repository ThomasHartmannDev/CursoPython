'''
Operadores relacionais
True ou False

5 > 4 = True
5 < 4 = False
5 <= 4 = False
5 >= 4 = True
3 != 2 : False
3 == 3 : True
2 == '2' : False 
'''
print('_=_=_=_Operadores relacionais_=_=_=_')
print(5 > 4) 
print(5 < 4)
print(5 <= 4)
print(5 >= 4)
print(3 != 2)
# Lembranco que (=) è apara atribuir valor a algo (a = 2 , A RECEBE 2), ja (==) è para IGUALDADE exemplos a baixo.
print(3 == 3)
print(2 == '2') # Note que 2 (int) è diferente de '2' (String)


print('_=_=_=_Operadores de atribuição_=_=_=_')
'''
Operadores de atribuição
'''

a = 3 #Definido que A recebe 3
a = a + 7 # A recebe A(com valor 3) + 7
print(a) # retorna 15
'''
note que o valor retornado no print è de 10 pois ele
esta somando 3 que esta atribuido a variavel A e somando 7 e atribuindo
o valor total (10) para A novamente.

'''

a += 5 # Neste caso estamos pegando o valor de A e acrecentando 5
'''
O metodo acima è uma abreviação do metodo usado na linha 30, seria o mesmo que fazer a = a + 5.

Valor de A passa a ser 10 devido a soma feita na linha 30.
logo na linha 39 è acrecentando 5 tornando A com valor 15
'''
print(a) # retorna 15


a -= 3 # Mesmo caso da linha 39 porem de maneira subtrativa.

print(a) # retorna valor 12

a *= 2 # Mesmo caso da linha 39 porem de maneira multiplicativa.

print(a) # retorna 24 
 
a /= 4 # vc ja entendeu nn ? agora è de maneira divisivel

print(a) #retorna 6

a %= 4 # maneira modular , mostra o Resto da divisão.

print(a) # retorna 2 

a **= 8 # maneira de exponenciação, potencia

print(a) # retorna 256

a //= 127 # maneira de divisão por inteiro

print(a) #retorna 2

