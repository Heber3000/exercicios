numeros = []

for i in range(10):
    num = int(input('Informe os números:'))
    numeros.append(num)

soma = 0
for j in numeros:
    soma+= j*j

print(f'{numeros}\nA soma dos quadrados {soma}')
