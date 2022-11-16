fatorial = int(input('Informe o valor fatorial:'))

while fatorial <= 0:
    print('Valor Impróprio')
    fatorial = int(input('Informe o valor fatorial:'))
else:
    print('Valor Aceito')

multi = 1
for i in range(1,1+fatorial):
    multi *=i



print(f'{fatorial}!={multi}')