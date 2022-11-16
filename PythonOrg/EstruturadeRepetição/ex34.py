num1=int(input('Informe o número:'))
print('')
while num1<=0:
    print('O número não pode ser menor ou igual a zero')
    num1 = int(input('Informe o número:'))
else:
    print('Valor valido')


primo = True
for i in range(2,num1):
    if num1 % i == 0:
        primo = False

if primo:
    print('Primo')
else:
    print('Não é primo')


