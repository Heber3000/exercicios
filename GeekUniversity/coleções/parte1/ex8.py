import random

lista =[]

for i in range(6):
    lista.append(random.randint(1,100))

print(f'{lista}\n{lista[::-1]}')