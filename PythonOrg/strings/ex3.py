nome = input('Informe seu nome:').title()
contador = 0


def nome_vertical(nome:str):
    for i in list(nome):
        print(i)


print(nome_vertical(nome))