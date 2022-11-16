A=[]
B=[]
C = []

import random

for i in range(5):
    A.append(random.randint(1,100))
    B.append(random.randint(1, 100))

for i, _ in enumerate(A):
    n = A[i]*B[i]
    C.append(n)

print(f'A:{A}\nB:{B}\nAxB:{C}')