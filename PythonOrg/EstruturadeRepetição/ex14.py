contador_par = 0
contador_impar = 0


for i in range(1,11):
    num = float(input('Informe o %sº número:' % i))
    if num % 2 == 0:
        contador_par +=1
    else:
        contador_impar +=1

print(f'Número de pares {contador_par}\nNúmero de impares {contador_impar}')


