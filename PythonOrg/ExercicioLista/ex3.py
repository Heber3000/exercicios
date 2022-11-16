lista = []
for i in range(1,5):
    notas = float(input('Informe a %sº' % i))
    lista.append(notas)

print(f'\nA Média é {sum(lista)/len(lista)}')