def log(function):

    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
        
    return decorator

@log #Chamando a função log.
def soma(x , y):
    return x + y
@log #Chamamando a função log.
def sub(x, y):
    return x - y



if __name__ == "__main__":
    print(soma(5,6))

    print(sub(5,y=6))