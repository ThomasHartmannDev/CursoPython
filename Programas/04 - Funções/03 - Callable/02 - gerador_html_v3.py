
def tag_bloco(conteudo,*args ,classe='success', inline = False):
    tag = 'span' if inline == True else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    '''
    Se conteudo não for um callble (uma função), ele irá usar args, caso seja uma função 
    ele irá executar a função normalmente.
    '''

    return f'<{tag} class={classe}> {html} </{tag}>'


def tag_lista(*itens): 
    lista = ''.join(f'<li>{item}</li>' for item in itens) 
    return f'<ul>{lista}</ul>' 


if __name__ == '__main__':
    print(tag_bloco(tag_lista,'Sabado','Domingo',classe='Info'))
    #Lembrando que quando possuimos um *args nos parametros da função não podemos 
    # usar o metodo posicional apos ele se não será enteirado para dentro da tupla.
    


