print(True or False)

print(7 != 3 and 3 > 4) # False 
''' 
para que retorne True ambas as afirmações devem ser verdadeiras.

7 != 3 è verdadeiro porem 3 > 4 è falso 

'''
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
print("Tabela verdade do AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
'''
não necessariamente deve se ter apenas 2 operarios pode se
ter por exemplo True and True and True
'''

print("Tabela verdade do OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")

'''
não necessariamente deve se ter apenas 2 operarios pode se
ter por exemplo True or True or True.
Porem se tivermos False or False or True, ira retornar verdadeiro
a sentença OR apenas retorna falso quando todos seus operarios forem False

'''
print("Tabela verdade do XOR (''OR Exclusivo'' Exclusivamente tem que ser um ou outro)")
print(True != True)
print(True != False)
print(False != True)
print(False != False)
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")

'''
Apenas um ou outro não se pode ter casos como True or True or True.
'''

print("Tabela verdade do NOT")
print(not True)
print(not False)
print(not 0)
print(not 1)
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
''' 
Observação: 0 significa True, e qualquer outro numero diferente de 0 significa False 

''' 

print("aplicação basica :")

Saldo = 1000
Salario = 4000
Despesas = 2967
# Troque para 3967 para ver que o resultado se transforma em Falso
Despesas_controladas = Salario - Despesas >= 0.2 * Salario
Saldo_positivo = Saldo > 0

meta = Saldo_positivo and Despesas_controladas
print(meta)

