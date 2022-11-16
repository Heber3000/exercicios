
lista = []

for i in range(6):
    num = int(input('Informe os valores:'))
    if num % 2 == 0:
        lista.append(num)

print(f'{lista}\n{lista[::-1]}')