num1 = int(input('Informe os valores:'))
num2 = int(input('Informe os valores:'))

while num1 > num2:
    print('O primeiro número não pode ser maior que o primeiro')
    num1 = int(input('Informe os valores:'))
    num2 = int(input('Informe os valores:'))
else:
    print('\nNúmeros aceitos')

multi =1
soma_par = 0

for i in range(num1,num2+1):
    if i % 2 == 0:

        soma_par +=i
    else:
        multi *= i

print(f'\nA soma dos pares é {soma_par}\nA multiplicação dos impares é {multi}')

