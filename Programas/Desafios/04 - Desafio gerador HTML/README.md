# Desafio - 4

## oque consiste o desafio ? 

Criar uma função que retorne HTML genérico, abrindo e fechando as tags, suportando quaisquer
atributos na tag e o seu conteúdo pode ser um texto ou uma lista com vários textos (ou outras tags
já como texto).
Caso encontre um atributo chamado de css, renomeá-lo para class. Isso é necessário por que class
é uma palavra reservada em Python, e não poderia ser usado como literal na chamada da função.

Exemplo de chamada da nova função ``tag``

```py
tag('p',
  tag('span', 'Curso de Python 3, por '),
  tag('strong', 'Thomas', id='jf'),
  tag('span', ' da '),
  tag('strong', 'Cod3r', id='ll'),
  tag('span', '.'),
  css='alert')

```