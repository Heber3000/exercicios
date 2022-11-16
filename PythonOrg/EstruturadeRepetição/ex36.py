num_mult = int(input('Informe o numero:'))

while num_mult == 0:
    print('O numero não pode ser zero')
    num_mult = int(input('Informe o numero:'))
else:
    print('Numero aceito\n')

num_comeco = int(input('Informe um número de começo da sequência: '))
num_final = int(input('Informe um número de final da sequência: '))

while num_comeco > num_final:
    print('O primeiro numero não pode ser maior que o primeiro:')
    num_comeco = int(input('Informe um número de começo da sequência: '))
    num_final = int(input('Informe um número de final da sequência: '))
else:
    print("\nValor aceito\n\n")

print(f'Montar a tabuada {num_mult}\nComeçar por {num_comeco}\nTerminar em {num_final}\n')

for i in range(num_comeco,num_final+1):
    print(f'{num_mult}x{i} = {num_mult*i}')
