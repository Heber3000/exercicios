notas = []

for nota in range(15):
    notas.append(float(input('Informe as %s:' % nota)))

print(f'A média geral é {sum(notas)/len(notas)}')