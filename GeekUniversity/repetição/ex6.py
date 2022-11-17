soma = 0
contador = 0
import random

for i in range(10):
    num = float(random.randint(1,10))
    print(num)
    soma +=1
    contador +=1

print(f'{soma/contador}')

