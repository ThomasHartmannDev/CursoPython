from decimal import Decimal, getcontext
import math
import sys



def circulo(Raio):  
    Pi = math.pi
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    return int(circunferencia), int(Area_circunferencia) 

def help():
    print(f'Você não passou nenhum argumento \nSintaxe correta: {sys.argv[0][-19:]} <Raio>') 

def is_float(valor): 
    try:
        float(valor)
    except ValueError:
        return False
 
    return True

if __name__ == "__main__":    
    is_float(sys.argv[1])

    if len(sys.argv) < 2:  
        help()
        sys.exit(1)
    elif is_float == False:
        help()
        print('Use apenas Numeros.')
        sys.exit(1)
    elif sys.argv[1].isalnum():#Verificamos se o valor inserido è uma letra com numero.
        help()
        print('Use apenas Numeros.')
        sys.exit(1)
    elif sys.argv[1].isalpha(): #Verificamos se o valor inserido è uma letra.
        help()
        print('Use apenas Numeros.')
        sys.exit(1)

    else:
        Raio = sys.argv[1].replace(',','.') 
        a = circulo(Raio)
        print(f'A circunferencia è de {a[0]} ea area da circunferencia è de {a[1]}') 
else: 
    pass
