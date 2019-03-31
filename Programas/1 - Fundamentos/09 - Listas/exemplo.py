lista = []  # Equivalente a um array em js ou c++(atè onde me lembro)
print(lista) #Note que o resultado sera uma lista vazia. 
print(len(lista)) # Tamanho da lista vai ser 0, pois não tem nada dentro dela. 
lista.append(1) 
lista.append(5)
'''
è feito uso do append para inserir coisas dentro de uma lista de forma programatica, neste caso inserimos 1 e 5.
(nos podemos ja definir valores dentro de uma lista não necessariamente se usa append para inserir algo dentro.
exemplo:
lista = [1,2,3,4,5,6,7,8,9,10]
) 
'''
print(lista)
print(len(lista)) # como foi adicionado coisas dentro da lista o tamanho dela se alterou. 

print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_')

nova_lista = [1, 5, 'Thomas','Daniel']
'''
Note que podemos utilizar tanto numeros em forma de int ou float e Strings.
'''
print(nova_lista) 
'''
não è uma boa Pratica do python utilizar listas com multiplas informações como exemplo ter nome e nota dos alunos.
a melhor forma è criar uma nova lista apenas para alunos e deixar outra lista apenas para notas.
'''
nova_lista.append('José')# adicionando String a lista.
nova_lista.remove(5)# Estamos removendo o numero 5 da lista e não o indice cinco.
print(nova_lista)

nova_lista.reverse()# a lista sera revertida, oque esta nova final passa para o começo e o que estava no começo vai para o final.
print(nova_lista)

nova_lista.append([1,2,3]) #Tambem è possivel criar listas dentro de uma outra lista. 
print(nova_lista)


print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_')
#Agora vamos acessar os dados de uma Lista.

Lista = [1, 5, 'Rebeca','Guilherme', 3.14]
print(Lista.index('Guilherme')) # A lista è uma estrutura indexada. Isto irá retornar onde esta "Guilherme" na lista.
print(Lista[3])

print('Rebeca' in Lista)# Note que podemos ""pesquisar"" dentro da lista utilizando IN para saber se esta ou não dentro da lista.
print('Pedro' in Lista)
print('Rebeca' not in Lista)

print(Lista[-1]) #pegamos o ultimo item da lista List[-2] o penultimo e assim por diante.
print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_')

lista2 = ['Ana', 'Lia', 'Rui', 'Paulo','dani']
print(lista2[1:3])# Vamos imprimir desde o index 1 atè o 3 apenas. 
del lista2[2]#Tambem podemos deletar um item da lista deste jeito.
print(lista2)

del lista2[1:] #deletar todos desde o index 1.
print(lista2)



