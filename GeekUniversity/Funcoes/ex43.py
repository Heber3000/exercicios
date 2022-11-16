from random import randint

def lista_aleatorio(tamanho):
    lista = []
    for i in range(tamanho):
        temp = randint(0,tamanho)
        if temp not in lista:
            lista.append(temp)
    return lista


numeros_gerados = lista_aleatorio(100)
numeros_gerados.sort()
print(numeros_gerados)