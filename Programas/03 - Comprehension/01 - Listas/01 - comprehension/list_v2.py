#[Expressão for item in list if condicional]

dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)
'''
if i % 2 == 0

se o modulo de i resultar 0 ele sera impresso dentro da lista
caso ao contrario não.

'''
# Forma ""Normal""
dobros_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)

print('Resultado da forma normal', dobros_dos_pares)

