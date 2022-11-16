base = int(input('Informe a base:'))

while base <= 0:
    print("\nValor Inválido")
    base = int(input('Informe a base:'))
else:
    print('Valor aceito')

expoente = int(input('Informe o expoente'))

while expoente <= 0:
    print("valor invalido")
    expoente = int(input('Informe o expoente'))
else:
    print('valor aceito')

potencia = 1
for i in range(1,expoente+1):
    potencia *=base

print(potencia)
