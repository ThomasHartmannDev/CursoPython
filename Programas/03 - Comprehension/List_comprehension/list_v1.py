'''
[Expressão for item in list if condicional]
'''

dobros = [i * 2 for i in range(10)]
print(dobros) 
'''
Dentro da propria lista è executado um for onde multiplica i dentro de uma Range 10
resultado da lista: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''

# Forma "normal"

dobros = []
for i in range(10):
    dobros.append(i * 2)

print('Resultado da forma normal', dobros)
