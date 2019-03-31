from decimal import Decimal, getcontext
import math
import sys 
def circulo(Raio):  
    Pi = math.pi
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    return int(circunferencia), int(Area_circunferencia) 


if __name__ == "__main__":
    print(type(sys.argv[1]))
    #python Programas/Fundamentos_projetos/Projeto_circunferencia/area_circulo_v8.py 100
    if len(sys.argv) < 2: # Caso não for passado o valor no argumento aponta o erro no console. 
        #Lembrando que Sys.argv è uma lista e quando è passado um argumento ele tem valor 2 ou a quantidade de argumentos passados + 1. 
        print(f'Você não passou nenhum argumento \nSintaxe correta: {sys.argv[0][-18:]} <Raio>') 
    else:
        Raio = sys.argv[1].replace(',','.') 
        a = circulo(Raio)
        print(f'A circunferencia è de {a[0]} ea area da circunferencia è de {a[1]}') 
else: 
    pass
