from decimal import Decimal, getcontext
import math

def circulo(Raio):  
    '''
    Criada uma DEF, uma função que recebe como parametro Raio e executa e imprime no console 
    os valores.
    '''
    Pi = math.pi
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    print(f'Acircunferencia è : {circunferencia} cm')
    print(f'A Area da circunferencia è : {Area_circunferencia} cm')


if __name__ == "__main__":

    Raio = input("Qual o raio da circunferencia ?").replace(',','.') 
    circulo(Raio)
else: 
    pass

