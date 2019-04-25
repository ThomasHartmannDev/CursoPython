def resultado_f1(Primeiro, Segundo, Terceiro, **ar):

    print(f'1) {Primeiro}')
    print(f'2) {Segundo}')
    print(f'3) {Terceiro}')


if __name__ == "__main__":
    podium = {
        'Primeiro': 'L. Hamilton',
        'Segundo':'M. Verstappen',
        'Terceiro':'S. Vettel'
    }

    resultado_f1(**podium)
    '''
    Exemplo de Unpacking fizemos uma Dict e passamos ela para dentro de um parametro.
    '''

