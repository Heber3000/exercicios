lista_A = []
lista_B = []

from random import randint



for i in range(8):
    lista_A.append(randint(1,100))
    lista_B.append(randint(1,100))

print(f'a){lista_A},soma = {sum(lista_A)}\nb){lista_B},soma={sum(lista_B)}')