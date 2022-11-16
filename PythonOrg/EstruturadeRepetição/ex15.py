limite_da_sequencia = int(input('Informe o limite da sequência:'))

while limite_da_sequencia<=0:
    limite_da_sequencia = int(input('\nInforme o limite da sequência:'))
else:
    print('Valor aceito\n')

primeiro = 0
segundo = 1
for n in range(1,limite_da_sequencia+1):
    terceiro = primeiro+segundo
    primeiro=segundo
    segundo=terceiro
    print(segundo)


