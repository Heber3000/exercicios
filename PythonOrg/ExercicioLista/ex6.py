
lista_medias = []
lista_notas = []
aprovados = 0

for i in range(10):
    for notas in range(1,5):
        nota = float(input('Informe a %sº:' % notas))
        lista_notas.append(nota)
    lista_medias.append(sum(lista_notas)/len(lista_notas))

    if lista_medias[i] >= 7:
        aprovados += 1

print(f'A quantidade de aprovados {aprovados}')























