
Nome = 'Thomas Hartmann'
print(Nome[0])# Podemos acessar qualquer letra determinando um numero dentro do parenteses.
# Lembrando que começa do numero 0, exemplo: 0 1 2 3 4 5 ... 
# String são imudavais.

print("marca d'agua") #usando aspas duplas.
#ou
print('marca d\'agua')# usando aspas simples.
# usando aspas simples è necessario colocar \ antes da aspa para ela não fechar e dar erro de sintaxe. 
print('marca d\'agua' == "marca d'agua") #podemos verificar que ambas são iguais

print('Nos podemos usar " apas duplas " dentro de \'Aspas simples\' ')

text = """ Teste
    para
            mostrar
    como se faz
            um texto
        de 
multiplas
        linhas """
# Assim como 3 aspas duplas tambem pode se usar 3 apas simples no lugr . 
print(text)
print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
"""
Note que o texto imprimido no console ele irá ficar do jeito proposto dentro da string.
em caso de String normal pode se usar \n para pular linha e \t para dar Tab 
    
"""

Nome = 'Thomas Hartmann'
'''
 0-T | 1-h | 2-o | 3-m | 4-a | 5-s | 6- (Espaço)| 
7-H | 8-a | 9-r | 10-t | 11-m | 12-a | 13-n | 14-n  

Tabelinha referente a letra eo numero. 
 
''' 
print(Nome[0])# mostrará a letra T 
print(Nome[5])# mostrará a letra S
print(Nome[6])# mostrará o espaço entre o nome eo sobrenome
print(Nome[-1]) #tambem è possivel pegar de trás para frente, neste caso começa do -1 neste caso N para tras
print(Nome[-10]) # Corresponde ao mesmo que a linha 41
print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
'''
Tenho 2 palavras, neste caso um nome e um sobrenome quero pegar apenas o sobre nome.
'''
print(Nome[7:]) #note que ele ia pegar da Letra H em diante

# ah mas agora eu quero so o nome.

print(Nome[:6]) # neste caso ele irá pegar atè a onde foi marcado no caso o espaço, mas note que ele não pega o espaço.

# Quero pegar apenas as 3 ultimas letras do nome eas 3 primeira do sobrenome.

print(Nome[3:10]) # Estamos pegando apenas da Letra M atè a letra R 

'''
Tambem podemos usar os valores negativos, mas è apenas recomentado quando se for pegar uma palava ou frase de um texto,
gigante ou uma frase comprida. 
'''

num = '1234567890'

print(num[::2])
'''
Não foi definido nenhum inicio nem um final, porem foi definido o Step, ele irá pegar toda informação de 2 em 2
Resultado desta print deve ser algo tipo 13580
'''
print(num[1::2]) # Definido inicio + step
print(num[:6:2]) # Definido onde parar + step
print(num[1:7:2]) # Definido inicio e fim + step
# Isso tambem funciona para letras mas usamos numeros para melhor exemplo e visualização.

print('_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_')
# passada rapida de transformação de string.

frase = 'Oi tudo bem ? Estou aprendendo python.'

frase = frase.upper() # usando o termo .upper() vc deixa toda a frase em maiusculo.
print(frase)
frase = frase.lower() # usando o termo .lower() vc deixa toda a frase em minusculo.
print(frase)
frase_split1 = frase.split() # o python irá quebrar todos os espaços e dividir dentro de uma lista a nossa frase.
print(frase_split1)
frase_split2 = frase.split('e') # iremos quebrar apartir de todo e contido na frase.
print(frase_split2) 

print(len(frase))# Usando len() nos podemos contar a quantidade de letras que temos em nossa frase.
print(len(frase_split1))#podemos contar por exemplo quantas palavras temos dentro de nossa frase.
