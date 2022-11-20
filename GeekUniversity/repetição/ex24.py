num1 = int(input('Informe os valores:'))
lista = []
if num1 > 0:
    for i in range(1,num1+1):
        if num1 % i == 0:
            print(f'O {num1} é divisivel o {i}')
            lista.append(i)
    lista.pop()
print(lista)
print(sum(lista))