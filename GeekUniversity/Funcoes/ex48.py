from random import randint

matriz = [[],[],[]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(randint(0, 99))

for l in range(3):
    for c in range(3):
        print(f'{[matriz[l][c]]}', end='      ')
    print()

def soma_diagonal(vetor):


    soma = vetor[0][0]  + vetor[1][1] +vetor[2][2]

    return soma


print(soma_diagonal(matriz))






