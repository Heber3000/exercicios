num1 = int(input('Informe o primeiro número:'))
num2 = int(input('Informe o segundo número:'))
num3 = int(input('Informe o terceiro número:'))

if num1 == num2 and num1 == num3:
    print('Os números são iguais')
else:
    if num1 > num2 and num1 > num3:
        print(f'O maior é o {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'O maior numero é {num2}')
    else:
        print(f'O maior é {num3}')
    print('')
    if num1 < num2 and num1 < num3:
        print(f'O menor é o {num1}')
    elif num2 < num1 and num2 < num3:
        print(f'O menor numero é {num2}')
    else:
        print(f'O menor é {num3}')



