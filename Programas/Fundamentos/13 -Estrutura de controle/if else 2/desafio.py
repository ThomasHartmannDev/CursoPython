def faixa_etaria(idade):
    if 0 <= idade <  18:
        return 'Menor de idade'
    
    elif idade in range(18,60):# Vai apenas atè 59
        return 'Adulto'

    elif idade in range(60,100):
        return 'Idoso'
    
    elif 100 <= idade <= 150 :
        return 'Centenário'
    
    elif idade >= 200:
        return 'Esta pessoa ja morreu.'

    else:
        return 'Idade invalida'

if __name__ == "__main__":
   for idade in (20, 10, 35, 50, 80, 100, 150, 230):
       print(faixa_etaria(idade))
    