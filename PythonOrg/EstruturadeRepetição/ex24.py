notas_qtd = int(input('Informe a quantidade de notas:'))

while notas_qtd<=0:
    print(f'não pode ser negativo e menor que 0')
    notas_qtd = int(input('Informe a quantidade de notas:'))
else:
    print('Valor aceito')


soma = 0
contador = 0
for i in range(1,notas_qtd+1):
    notas = float(input('Informe a %sº:' % i))
    soma += notas
    contador +=1


print(f'\nMédia: {soma/contador}')


if soma/contador > 7:
    aprovado = True
    print('Aprovado')
else:
    aprovado = False
    print('Reprovado')




