maior_valor = 0
contador = 0

for i in range(3):
    num = int(input('Informe os valores: '))
    if num > maior_valor:
        maior_valor = num
        contador =1
    elif maior_valor == num:
        contador += 1

print(f'O maior valor é {maior_valor} e aparece {contador} vezes')
