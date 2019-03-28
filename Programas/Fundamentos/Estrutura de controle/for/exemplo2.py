palavra = 'paralelepipedo'

for letra in palavra: 
    print(letra, end=',') # End faz com que coloque tudo na mesma linha, porem dividido por virgula

print('fim')

aprovados = ['Rafael', 'Pedro', 'Jose', 'Isabela', 'Julia']

for nome in aprovados: # Printa a lista de aprovados.
    print(nome)
print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')

for posicao, nome in enumerate(aprovados): #Enumera a lista de 0 ao valor total dela.
        print(posicao + 1, nome) #faz o print da posição e do nome. 

print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')

dias_semanas = ('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado')

for dia in dias_semanas:
        print(f'Hoje è {dia}') # faz prints de todos os dias da semana presente dentro da tupla.


# Veja o exemplo3.py






