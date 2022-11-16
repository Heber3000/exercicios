lista = []

temperatura = float(input('Informe as temperaturas(aperte 0 para encerrar):'))

while temperatura != 0:
    temperatura = float(input('Informe as temperaturas(aperte 0 para encerrar):'))
    lista.append(temperatura)
else:
    print('Encerrou')

lista.remove(0)

print(f'a máxima temperatura é de {max(lista)} a menor é {min(lista)}. A média de temperatura {sum(lista)/len(lista)}')
