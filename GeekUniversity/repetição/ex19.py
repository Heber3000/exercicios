num = int(input('Digite um número entre 100 e 999:'))

while num < 100 or num > 999:
    print('O numero tem que estar entre 100 e 999')
    num = int(input('Digite um número entre 100 e 999:'))
else:
    print('\nNúmero aceito')

for posicao_digito in enumerate(num.__str__()):
    print(posicao_digito)