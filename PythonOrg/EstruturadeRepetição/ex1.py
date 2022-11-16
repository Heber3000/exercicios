nota = float(input('Informe uma nota de 0 a 10:'))

while nota < 0 or nota>10:
    print('\nO valor tem que estar entre 0 e 10:')
    nota = float(input('Informe uma nota de 0 a 10:'))
else:
    print('Valor aceito:')