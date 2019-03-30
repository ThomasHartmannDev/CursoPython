def get_dia_da_semana(dia):
    dias = {
        1 : 'Domingo',
        2 : 'Segunda',
        3 : 'Terça',
        4 : 'Quarta',
        5 : 'Quinta',
        6 : 'Sexta',
        7 : 'Sabado',
    }
    return dias.get(dia,'** Dia invalido **')


if __name__ == "__main__":
    for dia in range(0,9):
        if dia == 7 or dia == 1:
            print(f'{dia} : {get_dia_da_semana(dia)}, è um dia durante o final de semana')
        elif dia == 0 or dia == 8:
            print(f'{dia} : {get_dia_da_semana(dia)}')
        else:
            print(f'{dia} : {get_dia_da_semana(dia)}, è um dia durante a semana')
