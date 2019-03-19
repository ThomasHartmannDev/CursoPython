from decimal import Decimal, getcontext
import math

Pi = math.pi
Raio = 5
print(Pi)
getcontext().prec = 4
circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
Area_circunferencia = Decimal(Pi) * Decimal(Raio) **2

print(f'Acircunferencia è : {circunferencia} cm')
print(f'A Area da circunferencia è : {Area_circunferencia} cm')