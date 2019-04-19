def tag_bloco(texto, classe='success', inline = False): #Adicionamos inline com valor padrão falso.

    tag = 'span' if inline == True else 'div'
    '''
    Caso o valor de inline seja True retorna 'span' se não retorna div

    '''
    return f'<{tag} class={classe}> {texto} </{tag}>'


if __name__ == '__main__':

    print(tag_bloco('Inline e classe','info',True))#Posicional.
    print(tag_bloco('Inline True',inline=True))#Note que misturamos posicional com nomeado. 
    print(tag_bloco(inline=True,texto='Texto',classe='Fade'))#Note que alteramos toda a ordem.
