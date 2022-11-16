par = []
impar = []
lista = []

for i in range(1,10):
    num = float(input('Informe a %sº' % i))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'\n{lista}\n{par}\n{impar}')
