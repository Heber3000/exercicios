limite = int(input('Informe o limite da sequência:'))

while limite <= 0 or limite >= 1000:
    print('O valor não pode ser negativo ou maior que 1000')
    limite = int(input('Informe o limite da sequência:'))
else:
    print(f'{limite}Valor válido')





lista = []

for i in range(1,1501):
    lista.append(i)

print(f'\nMaior {max(lista)}\nMenor {min(lista)}\nSoma {sum(lista)}')