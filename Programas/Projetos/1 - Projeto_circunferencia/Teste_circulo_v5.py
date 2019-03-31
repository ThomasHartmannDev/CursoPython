import area_circulo_v5 # importa o modulo 

area_circulo_v5.circulo(10) # Usa a função circulo passando parametro 10. 

'''
Se importamos apenas area_circulo_v5 precisamos usar area_circulo_v5.circulo()
mas se fizermos igual o exemplo a baixo usamos apenas circulo()
'''
from area_circulo_v5 import circulo

a = input('Qual o Raio ?')
circulo(a)