import random
lista = []
contador = 0


for i in range(5):
    num = int(input('Informe os valores:'))
    lista.append(num)
    print(lista)

x = set(lista)

if len(x) < len(lista):
    print('Há numeros repetidos')
else:
    print('Não há numero repetidos')




