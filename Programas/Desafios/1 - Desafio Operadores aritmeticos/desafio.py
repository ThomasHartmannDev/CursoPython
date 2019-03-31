salario = 3450.45
despesas = 2456.2

um_porcento = salario // 100
'''
divide o valor do salario por 100, obtemos um valor inteiro, neste caso para evitar casas decimais
foi usado // para obter um valor aprocimado sem virgula
'''

print('um porcento do salario equivale a {} Reais'.format(um_porcento))

'''
Uso do .format(um_porcento), em python format è usado para inserir dados como exemplo numeros
dentro de uma string ja que não è possivel utilizar ""print('um porcento equivale a ' + um_porcento + ' reais')
como visto na linha 10, para inserir usa se {} dentro da string, futuramente veremos melhor sobre
'''

porcentagem_final = despesas // um_porcento
'''
divide o valor das despesas pelo valor de um_porcento para resultar o valor de 72.0, um valor aproximado
''' 

print('A porcentagem gasta do salario è de {}% aproximadamente'.format(porcentagem_final))

print('=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=')

'''
Vamos fazer agora com os valores Exatos sem uso da divisão com // 

Como o programa executa de cima para baixo podemos atribuir valores diferentes as mesmas variaveis
a partir daki o codigo è o mesmo com a diferença de que è feito com os valores inteiros sem estarem arredondados.
'''

um_porcento = salario / 100

print('um porcento do salario equivale a {} Reais'.format(um_porcento))

porcentagem_final = despesas / um_porcento

print('A porcentagem gasta do salario è de {}% aproximadamente'.format(porcentagem_final))

'''
A saida deve ser algo do tipo : 

um porcento do salario equivale a 34.0 Reais
A porcentagem gasta do salario è de 72.0% aproximadamente
=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
um porcento do salario equivale a 34.5045 Reais
A porcentagem gasta do salario è de 71.1849179092582% aproximadamente
''' 