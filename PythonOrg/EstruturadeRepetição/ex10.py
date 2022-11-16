num1 = int(input('Informe um número inteiro:'))
num2 = int(input('Informe um segundo numero:'))

while num1 >= num2:
    print('O primeiro número não pode ser maior que o segundo')
    num1 = int(input('Informe um número inteiro:'))
    num2 = int(input('Informe um segundo numero:'))
else:
    print('\nIntervalo aceito:\n')
    for i in range(num1,num2+1):
        print(i)

