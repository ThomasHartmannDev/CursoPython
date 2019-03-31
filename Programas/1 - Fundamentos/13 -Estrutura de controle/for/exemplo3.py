produto = {
    'Nome':'Caneta Chique',
    'preco': 14.99,
    'importada':True,
    'estoque': 793
}

for chaves in produto:
    print(chaves)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave , ' = ', valor )


