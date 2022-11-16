n_pessoas = int(input('Informe a quantidade de pessoas com cálculo de idade:'))

while n_pessoas <0:
    print('O valor não pode ser negativo')
    n_pessoas = int(input('Informe a quantidade de notas:'))
else:
    print('\nValor Aceito')

contador = 0
soma = 0
for i in range(1,n_pessoas+1):
    idade = int(input('Informe %sº :' % i))
    soma += idade
    contador += 1

print(f'\nA MÉDIA é {soma/contador}')

if soma/contador <= 25:
    print(f'A média de idades é de 0 a 25 anos')
elif soma/contador <= 60:
    print(f'A média de idades é de 26 a 60 anos')
else:
    print(f'está acima dos 60')

