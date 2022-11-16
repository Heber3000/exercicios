matriz = [[],[],[],[]]
contador = 0
import random

for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(random.randint(1,100))
        if matriz[linha][coluna] > 10:
            contador += 1

for l in range(4):
    for c in range(4):
        print(f'{[matriz[l][c]]}',end='  ')
    print()

print(f'numeros maiores que 10 é {contador}')


