from decimal import Decimal, getcontext
import math

def circulo(Raio):  
    Pi = math.pi
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    return int(circunferencia), int(Area_circunferencia) #Agora a função ela RETORNA os valores. 


if __name__ == "__main__":

    Raio = input("Qual o raio da circunferencia ?").replace(',','.') 
    a = circulo(Raio)
    print(f'A circunferencia è de {a[0]} ea area da circunferencia è de {a[1]}') 
else: 
    pass

