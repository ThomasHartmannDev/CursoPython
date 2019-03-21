from decimal import Decimal, getcontext
import math

if __name__ == "__main__": 
    '''
    è criada uma condicional If(se) para executar o codigo se quem estiver executando for a main
    no caso executando este arquivo diretamente e não chamado por outro arquivo.
    '''

    Pi = math.pi
    Raio = input("Qual o raio da circunferencia ?").replace(',','.') 
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    print(f'Acircunferencia è : {circunferencia} cm')
    print(f'A Area da circunferencia è : {Area_circunferencia} cm')
else:
    '''
    Condicional Else (se não) 
    pass (não faz nada :v)
    '''
    pass

