valor_maior=valor_menor =int(input('Digite o primeiro número:'))

for i in range(2,11):
    num = int(input('Informe os valores:'))
    if num > valor_maior:
        valor_maior = num
    else:
        valor_menor = num

print(f'maior {valor_maior}\nmenor {valor_menor}')