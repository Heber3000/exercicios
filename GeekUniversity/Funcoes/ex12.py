def soma_algorismo(numero):
    soma = 0
    num = list(str(numero))
    for i in range(len(num)):
        print(int(num[i]))
        soma = soma + int(num[i])
    return print(f'-------------+\n{soma}')


numero = int(input('Informe o número:'))

while numero <= 0:
    print('Valor Não Pode ser igual a zero')
    numero = int(input('Informe o número:'))
    print('')
else:
    print('\nValor válido')

print(soma_algorismo(numero))

