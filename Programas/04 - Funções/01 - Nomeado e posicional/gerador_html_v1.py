def tag_bloco(texto, classe='success'):
    return f'<div class={classe}> {texto} </div>'


if __name__ == '__main__':

    assert tag_bloco('Incluido com sucesso') == '<div class=success> Incluido com sucesso </div>'

    assert tag_bloco('Impossivel Excluir !!', 'Warning') == '<div class=Warning> Impossivel Excluir !! </div>'
    
    '''
    assert funciona da seguinte maneira, caso a afirmação dele seja identica ou no caso seja True.
    ele não retorna nada e não gera erro, caso acontece de não ser uma afirmação identica ele ira gerar um erro.

    '''

    print(tag_bloco('Bloco')) # Note que usamos a posicional para definir oque era pra ser escrito.
    #Como foi definido um valor default para classe sendo ela success não precisamos definir ela caso não queira.
    
