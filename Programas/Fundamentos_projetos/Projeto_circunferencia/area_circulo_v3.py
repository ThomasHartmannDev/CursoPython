from decimal import Decimal, getcontext
import math

Pi = math.pi
Raio = input("Qual o raio da circunferencia ?").replace(',','.') # input para pegar informação do usuario.
'''
Como python não aceita , precisa ser 2.5 e não 2,5 usamos o replace para transformar a , em um . 
''' 
getcontext().prec = 4
circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
Area_circunferencia = Decimal(Pi) * Decimal(Raio) **2

print(f'Acircunferencia è : {circunferencia} cm')
print(f'A Area da circunferencia è : {Area_circunferencia} cm')
