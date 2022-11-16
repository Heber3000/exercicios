lista = []

import random

for i in range(5):
    lista.append(random.randint(1,100))

print(f'{lista}\nmaior:{max(lista)}\nmenor:{min(lista)}\nmedia:{sum(lista)/len(lista)}')