def tag_bloco(conteudo, classe='success', inline = False):
    tag = 'span' if inline == True else 'div'

    return f'<{tag} class={classe}> {conteudo} </{tag}>'


def tag_lista(*itens): # Fazendo uso do packing a partir do *itens
    lista = ''.join(f'<li>{item}</li>' for item in itens) #Usando metodo generator.
    return f'<ul>{lista}</ul>' 


if __name__ == '__main__':
    lista = tag_lista('Item 1','Item 2','Item 3')
    print(tag_bloco(lista, 'info')) 

    print(tag_bloco(tag_lista('Thomas','Livia','Julia'),classe='Info'))