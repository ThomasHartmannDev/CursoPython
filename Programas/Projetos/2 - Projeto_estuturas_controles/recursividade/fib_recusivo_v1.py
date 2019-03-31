
def fibonnaci(quantidade,sequencia = (0,1)):
    #IMPORTENTE CONDIçÃO DE PARADA
    if quantidade > 990:
        return 'Quantidade limite è de 990'
    if len(sequencia) == quantidade:
        return sequencia
    return fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == "__main__":

    for fib in fibonnaci(995):
        #listar os 20 primeiros valores da sequencia.
        print(fib, end=' ')