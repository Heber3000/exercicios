a = []
b = []
c = []

from random import randint as aleatorio

for i in range(10):
    a.append(aleatorio(1,50))
    b.append(aleatorio(1, 50))

for i, _ in enumerate(a):
    n = a[i] - b[i]
    c.append(n)



print(f'vetorA: {a}\nVetorB: {b}\nVetorC: {c}')