precoMercadoria = float(input('Informe o preço da mercadoria:'))
soma = 0

while precoMercadoria != 0:
    precoMercadoria = float(input('Informe o preço da mercadoria:'))
    soma += precoMercadoria
else:
    print(F'\nO total de Mercadoria R${soma}')

dinheiro_recebido = float(input('Informe o valor pago:'))

print(f'\ncompras:R${soma}\n{dinheiro_recebido}\n--------------------\n{dinheiro_recebido-soma}')

