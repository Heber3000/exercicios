
def lista_par_impar(n):
    lista_par = []
    lista_impar = []
    for i in range(1,n+1):
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return f'Lista Par {lista_par}\nLista Impar {lista_impar}'

print(lista_par_impar(100))