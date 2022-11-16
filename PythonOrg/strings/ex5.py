nome = input('Informe seu nome:').upper()
lista = list(nome)

for i in range(len(nome)-1,-1,-1):
    for j in range(0,1+i):
        print((lista[j]),end='')
    print()
