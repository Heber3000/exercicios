import random

lista = []
contador_par = 0
for i in range(10):
    lista.append(random.randint(1,20))
    if lista[i] % 2:
        contador_par += 1

print(f'Lista{lista}\nQuantidade de pares {contador_par}',)