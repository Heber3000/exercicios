alturas = []
numeros = []

for i in range(2):
    numeros.append(int(input(f'Informe o número do aluno {i+1}º:')))
    alturas.append(float(input(f'Informe a alturas do aluno {i+1}º:')))

print(f'O maior aluno é {max(alturas)} e está na posição {numeros[alturas.index(max(alturas))]}')
