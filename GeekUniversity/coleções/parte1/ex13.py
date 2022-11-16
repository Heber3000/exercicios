lista = []

import random

for i in range(5):
    lista.append(random.randint(1,100))

print(f'{lista}\nPosição Maior:{lista.index(max(lista))}\nPosição Menor:{lista.index(min(lista))}')

