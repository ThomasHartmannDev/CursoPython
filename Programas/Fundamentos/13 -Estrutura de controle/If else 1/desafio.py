'''
Entrada     | Resultado
------------|----------------
10.0 à 9.1  |   A
9.0  à 8.1  |   A-
8.0  à 7.1  |   B
7.0  à 6.1  |   B-
6.0  à 5.1  |   C
5.0  à 4.1  |   C-
4.0  à 3.1  |   D
3.0  à 2.1  |   D-
2.0  à 1.1  |   E
1.0  à 0.0  |   E-

Para Notas maiores que 10, menores que 0 e Letras Retornar invalido.
'''
def calc_nota(valor):
    try:
        nota = valor.replace(',','.')
        nota = float(nota)
    except:
        return 'Insira apenas Numeros.'
    if nota > 10 or nota < 0:
        return 'Nota Invalida'

    elif nota >= 9.1:
        return 'A'

    elif nota >= 8.1:
        return 'A-'

    elif nota >= 7.1:
        return 'B'

    elif nota >= 6.1:
        return 'B-'

    elif nota >= 5.1:
        return 'C'

    elif nota >= 4.1:
        return 'C-'

    elif nota >= 3.1:
        return 'D'

    elif nota >= 2.1:
        return 'D-'
    
    elif nota >= 1.1:
        return 'E'

    elif nota >= 0:
        return 'E-'

a = input('Insira a nota do Aluno: ')

nota_do_aluno = calc_nota(a)
if nota_do_aluno == 'Nota Invalida':
    print(f'{a} = {nota_do_aluno}')
else:
    print(f'A nota {a} é equivalente a letra : {nota_do_aluno}')
