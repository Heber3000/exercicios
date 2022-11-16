soma = 0
contador = 0
for i in range(1,6):
    num = int(input('Informe um número:'))
    soma += num
    contador +=1

print(f'\nMédia {soma/contador}')
