nome = input('Informe seu nome:').title()
lista = list(nome)

for i in range(len(nome)):
    for j in range(0,1+i):
        print(lista[j],end='')
    print()







