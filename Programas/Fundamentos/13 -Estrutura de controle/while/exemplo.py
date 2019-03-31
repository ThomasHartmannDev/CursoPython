'''
ele irá printar infinitamente no console "infinito"
while True:
    print('infinito')
'''

while True:
    print('infinito')
    break # Usando Break ele quebra o laço e termina ele. 

from random import randint # è ideal que seja sempre importado logo no começo do projeto, estou importando aki para ficar algo cronologico.

numero_informado = -1 # numero definido deve ser algo fora das possibilidades do numero secreto.
numero_secreto = randint(0,9)# è sortiado um numero de 0 a 9 

while numero_informado != numero_secreto: #enquanto o numero informado for diferente do numero secredo não termina o laço, ele executa infinitamente.
    numero_informado = int(input('Informe o número: '))

print(f'O número secredo {numero_secreto} foi descoberto')
