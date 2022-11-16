quantidade_cds = int(input('Informe a quantidade de Cds:'))
print('')
while quantidade_cds <=0:
    print('O valor não pode ser maior ou igual a zero')
    quantidade_cds = int(input('Informe a quantidade de Cds:'))
else:
    print('O valor aceito\n')

soma = 0
contador = 0
for i in range(1,quantidade_cds+1):
    preco = int(input('O valor em do %sº' % i))
    soma += preco
    contador += 1

print(f'A média de preços dos Cds R${"%.2f" % float(soma/contador)}')

