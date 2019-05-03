class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

d1 = Data(30, 8, 2001)
print(d1)

d2 = Data(dia= 10, mes= 12, ano = 2019)
print(d2)