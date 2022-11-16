lista = []

for i in range(10):
    num = float(input('Informe 10 numeros'))
    lista.append(num)

print(f'Maior {max(lista)}\nMenor {min(lista)}')