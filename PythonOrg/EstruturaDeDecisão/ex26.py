opcao= input('Escolha a opção de gasolina G(Gasolina) ou (Alcool):').upper()
qtd_litros = float(input('Informe a quantidade em litros:'))
desconto = 0
preco = 0

if opcao == 'A':
    preco = 1.9
    if qtd_litros <= 20:
        desconto = 0.97
    else:
        desconto = 0.95
elif opcao == 'B':
    preco = 2.9
    if qtd_litros <= 20:
        desconto = 0.96
    else:
        desconto = 0.94
else:
    print('opção inválida')


print(f'Quantidade a ser pago {qtd_litros*preco*desconto}')


