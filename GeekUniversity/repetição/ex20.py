lista = []

num = int(input('Informe os valores (Digite 1000 para encerrar):'))

while num != 1000:
    num = int(input('Informe os valores (Digite 1000 para encerrar):'))
    if num % 2 == 0:
        lista.append(num)
else:
    lista.pop()
    for i in lista:
        print(i)
