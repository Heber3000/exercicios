A=[]
B=[]
C_par=[]
C_impar=[]

import random

for i in range(10):
    A.append(random.randint(1,100))
    B.append(random.randint(1, 100))

for valor in A:
    if valor % 2 == 0:
        C_par.append(valor)

for valor in B:
    if valor % 2 != 0:
        C_impar.append(valor)

print(f'Vetor A:{A}\nVetor B{B}\nVetor Par {C_par}\nVetor Impar {C_impar}')