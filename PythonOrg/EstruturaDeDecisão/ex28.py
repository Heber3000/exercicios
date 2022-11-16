opcao_carne = input('selecione uma opção de carne F-Filé Duplo, A-ALcatra e P-Picanha:').upper()

if opcao_carne != 'F' and opcao_carne != 'A' and opcao_carne != 'P':
    print('Opção Inválida')
else:
    quantidade_carne=float(input('Informe a quantidade carnes kg:'))
    tipo_de_carne = ''
    if opcao_carne == 'F':
        tipo_de_carne = 'Filé Duplo'
        if quantidade_carne <= 5:
            preco = quantidade_carne*4.9
        else:
            preco = quantidade_carne*5.8
    elif opcao_carne == 'A':
        tipo_de_carne = 'Alcatra'
        if quantidade_carne <= 5:
            preco = quantidade_carne*5.9
        else:
            preco = quantidade_carne * 6.8
    else:
        tipo_de_carne = 'Picanha'
        if quantidade_carne <= 5:
            preco = quantidade_carne*6.9
        else:
            preco = quantidade_carne*7.8

    cartao = input('Pagamento com cartão S-sim ou N-não').upper()


    if cartao == 'S':
        opcao_pagamento = 'Cartão'
        desconto = 0.05
    else:
        desconto = 0
        opcao_pagamento = 'dinheiro'

print(f'\n      Cupom Fiscal\nCarne {tipo_de_carne}\nQuantidade de carne {quantidade_carne}\nMeio de pagamento {opcao_pagamento}\n'
      f'\n{preco-preco*desconto}')







