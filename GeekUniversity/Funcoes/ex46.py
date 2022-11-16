from random import randint

lista = []
for i in range(1,10):
    num=randint(1,100)
    lista.append(int(num))




def impressao(vetor:list):
    return f'lista normal {vetor}'


def impressao_inversa(vetor:list):
    return f'lista inversa {vetor[::-1]}'


def media(vetor:list):
    return f'A média é {"%.2f" % float(sum(vetor)/len(vetor))}'

print(f'{impressao(lista)}\n{impressao_inversa(lista)}\n{media(lista)}')
