import random

lista = []

for i in range(10):
    lista.append(random.randint(0,50))



nova_lista = []

for i in lista:
    if i % 2 != 0:
        nova_lista.append(i)

print(f'{lista}\n{nova_lista}')

