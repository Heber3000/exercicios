lista = []

for i in range(10):
    num = float(input('Informe 10 numeros'))
    lista.append(num)

print(lista)

print(f'Maior é {max(lista)}\nposição: {lista.index(max(lista))}')