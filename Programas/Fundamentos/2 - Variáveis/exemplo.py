a = 10 # Neste caso A recebe 10 (int)

b = 5.2 #Neste caso B recebe 5.2 (float)
''' 
Python não necessita a tipagem, exemplo em C a variavel B deveria ser 
definida com float B = 5.2 e A como int A = 10.
'''
print(a + b) # Valor da soma será 15.2 

'''
Seguindo uma forma linear de cima para baixo
nós podemos alterar A para uma String

'''

a = 'A virou uma String'
print(a)

'''
print(a + b)

nós não podemos fazer isso pois o python não soma um valor INT ou FLOAT (b) a um valor STRING (a).

caso B tambem fosse alterado funcionaria normalmente. 
'''
b = ' ,B tambem virou uma String'

print(a + b) # Tambem podemos "Somar" Strings, mas isso tem outro nome Concatenar.

''' 
Resultado final em seu console deve ser algo parecido com isto.

15.2
A virou uma String
A virou uma String ,B tambem virou uma String

''' 