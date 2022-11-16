numeros = []
for i in range(4):
    num = int(input('informe os valores:'))
    numeros.append(num)

soma = 0
mult= 1
for j in numeros:
    soma +=j
    mult *=j

print(f'{numeros}\n\nsoma:{soma},multiplicação:{mult}')