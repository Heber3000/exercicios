num1 = int(input('Informe o valor inteiro:'))
soma = 0

for i in range(1,1000):
    if i % 3 == 0:
        print(f'divisores de 3 é {i}')
        soma +=i
    if i % 5 == 0:
        print(f'divisores de 5 é {i}')
        soma +=i

print(f'Soma {soma}')