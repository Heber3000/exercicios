num = int(input('Informe um valor positivo:'))

while num <= 0:
    print(f'\nO número tem que ser positivo')
    num = int(input('Informe um valor positivo:'))
else:
    print('O Valor tem que ser positivo')

primo = True
for i in range(1,num+1):
    if i % 2== 0:
        primo = False

if primo:
    print(f'É primo\nEle é divisivel {1} e {num}')

else:
    print('Não é primo')