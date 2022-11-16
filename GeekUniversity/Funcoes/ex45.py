import math

def desvio_padrao(n):
    lista = []

    for i in range(1,n+1):
        lista.append(i)
    media = sum(lista)/len(lista)

    for j in range(1,n+1):
        j +=j

        return  math.sqrt((j - media)**2)

print(desvio_padrao(10))

