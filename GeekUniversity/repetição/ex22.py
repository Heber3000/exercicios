soma = 0
contador = 0

num=float(input('Informe os números:'))

while num > 10 or num >20:
    num = float(input('Informe os números:'))
    soma +=num
    contador += 1
else:
    print('encerrou')

print(f'A média é {"%.2f" % (soma/contador)}')