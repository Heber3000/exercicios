soma = 0
for i in range(10):
    num1 = int(input('Informe o número:'))
    if num1 > 0:
        soma += num1
        print(f'+{num1}:soma {soma}')