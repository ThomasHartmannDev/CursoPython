def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao}: {piloto}')
'''
Usando ** ao invez de criar uma tupla criamos uma dict, mas segue o mesmo raciocinio das tuplas.
'''

if __name__ == "__main__":

    resultado_f1(Primeiro = 'L. Hamilton',Segundo = 'M. Verstappen',Terceiro ='S. Vettel')
    # Fazemos definição de chave valor.  
