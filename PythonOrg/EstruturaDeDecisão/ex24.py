
print('\nescola as opções:\na)Par ou Impar.\nb)positivo ou negativo.\nc)inteiro ou decimal\n')
opcao = input('\nEscolha uma opção:').upper()


if opcao != 'A' and opcao != 'B' and opcao != 'C':
    print('Valor Inválido')
else:
    num1 = float(input('\nInforme o primeiro número:'))
    if opcao == 'A':
        if num1 % 2 == 0:
            print('Par')
        else:
            print('Impar')
    elif opcao == 'B':
        if num1 < 0:
            print('Negativo')
        else:
            print('Positivo')
    elif opcao == 'C':
        if num1 == int(num1):
            print('Inteiro')
        else:
            print('Decimal')







