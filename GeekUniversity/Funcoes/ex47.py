import random

matriz = [[],[],[],[]]
for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(random.randint(0,20))
print(matriz)


for l in range(4):
    for c in range(4):
        print(f'[{matriz[l][c]:^7}]', end = '')
    print()


def matriz4x4(lista):
    contador = 0
    for linha in range(len(lista)):
        for coluna in range(len(lista)):
            if lista[linha][coluna] > 10:
                contador += 1
    return f'\nNa matriz há {contador}'


print(matriz4x4(matriz))







