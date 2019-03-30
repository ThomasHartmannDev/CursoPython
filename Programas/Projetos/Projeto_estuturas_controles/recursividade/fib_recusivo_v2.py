
def fibonnaci(quantidade,sequencia = (0,1)):
    #IMPORTENTE CONDIçÃO DE PARADA
    if quantidade > 990:
        return 'Quantidade limite è de 990'
    # Retorne sequencia se sequencia for igual a quantidade senão, executa regra de fibonacci
    return sequencia if len(sequencia) == quantidade else \
        fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == "__main__":

    for fib in fibonnaci(995):
        #listar os 20 primeiros valores da sequencia.
        print(fib, end=' ')