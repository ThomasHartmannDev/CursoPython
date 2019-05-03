def todos_params(*args,**Kwargs):
    print(f'{args}')
    print(f'{Kwargs}')


if __name__ == "__main__":
    todos_params('A','B','C')#Parametros posicionais
    # (1, 2, 3)
    # {}
    
    todos_params(1,2,3, Legal = True, valor = 10)#Parametros posicionais e nomeados.
    # (1, 2, 3) 
    # {'Legal': True, 'valor': 10}

    todos_params('Livia', False, [1,2,3,4,5], Amor = True, Tamanho = 'M')
    # ('Livia', False, [1, 2, 3, 4, 5])
    # {'Amor': True, 'Tamanho': 'M'}
    