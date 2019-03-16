from decimal import Decimal , getcontext #Aqui faremos o import do decimal para uso de decimais.


a = Decimal(1) / Decimal(7)

print(a)
'''
Note que o resultado sera um valor gigantesco podemos usar o getcontext para pegar atè onde nós
precisamos ou queremos.
'''

getcontext().prec = 4 # Aki nos colocamos a precisão, neste caso aparecerá apenas 4 numeros. 
a = Decimal(1) / Decimal(7) #Precisamos definir novamente a variavel A para ela se adequar ao getcontext().prec

print(a)

b = Decimal('2.1')  + Decimal('2.2')

print(b) # Note que tambem funciona com String. mas a string deve ter numeros e não letras.


