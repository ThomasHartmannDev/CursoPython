
class Potencia:
    #Calcular potencia especifica de algum numero.
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente

if __name__ == "__main__":
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3 ** 2 => {quadrado(3)}')
        print(f'5 ** 2 => {cubo(5)}')

# Apenas um exemplo de que objeto pode entrar em callable, mais para frente terá
# uma melhor explicação sobre class e tudo mais. 