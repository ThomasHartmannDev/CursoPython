'''
Faremos uso do .is_integer para descobrir se o numero ou variavel è um inteiro. 
retorno True or False

o is_integer(), entende que 5.0 è um inteiro. não do tipo INT mas o conteudo è um inteiro.
ja no caso de 5.5 ele entende que não è um inteiro.
veja o exemplo a baixo.
'''

a = 5.0
b = 5.5
print('a variavel A è um inteiro ? Resposta: {}'.format(a.is_integer()))
print('a variavel B è um inteiro ? Resposta: {}'.format(b.is_integer()))
'''
o is_interger so funciona apenas com tipo Float.
caso vc substitua a variavel A ou B por apenas 5 por exemplo irá gerar um erro no console e não vai ser executado.

'''
print(2.2 + 1.1)
'''
Note que esta soma simples de valores decimais ira resultar 3.3000000000000003, quando era pra resultar simplesmente 
3.3, isso ocorre em varias linguagems e no python não è diferente, para isso não ocorrer precisamos importar
uma biblioteca decimal.
Agora vamos para o exemplo2.py  
'''





