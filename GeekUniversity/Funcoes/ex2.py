



def data(dia,mes,ano):
    dicionario = {1: 'JAN', 2: 'FEV', 3: 'MAR', 4: 'ABR', 5: 'MAI', 6: 'JUN', 7: 'JUL', 8: 'AGO', 9: 'SET', 10: 'OUT',
                  11: 'NOV', 12: 'DEZ'}
    return print(f'{dia} de {dicionario.get(mes)} de {ano}')

print(data(11,11,2022))