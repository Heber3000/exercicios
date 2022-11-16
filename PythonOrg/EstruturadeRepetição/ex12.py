numero = int(input('Informe o número de entre 1 a 10:'))
contador = 0

while numero <= 0 or numero > 10:
    numero = int(input('Informe o número de entre 1 a 10:'))
    print("")
else:
    for i in range(1,11):
        print(f'{numero}X{i}= {numero*i}')