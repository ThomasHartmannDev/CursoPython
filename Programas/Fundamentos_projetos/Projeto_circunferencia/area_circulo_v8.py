from decimal import Decimal, getcontext
import math
import sys #importamos SYS 

def circulo(Raio):  
    Pi = math.pi
    getcontext().prec = 4
    circunferencia = 2 * Decimal(Pi) * Decimal(Raio)
    Area_circunferencia = Decimal(Pi) * Decimal(Raio) ** 2

    return int(circunferencia), int(Area_circunferencia) #Agora a função ela RETORNA os valores. 


if __name__ == "__main__":
    print(sys.argv[1]) # pegamos o argumento passado na inicialização do projeto 
    '''
    inicializamos o projeto passando argumento 100, no caso 100cm de raio
    python Programas/Fundamentos_projetos/Projeto_circunferencia/area_circulo_v8.py 100
    '''
    Raio = sys.argv[1].replace(',','.') #input("Qual o raio da circunferencia ?").replace(',','.') 
    a = circulo(Raio)
    print(f'A circunferencia è de {a[0]} ea area da circunferencia è de {a[1]}') 
else: 
    pass
