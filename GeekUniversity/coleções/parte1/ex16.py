lista = []
for i in range(5):
    lista.append(float(input('Informe os valores:')))

print(lista)
opcao = int(input('\nescolha uma das opções\n0:encerrar\n1:ordem direta\n2:orden inversa'
                  ':'))

if opcao == 0:
    print('Encerrar programa')
elif opcao == 1:
    print(lista)
elif opcao == 2:
    print(lista[::-1])
else:
    print('Valor Inválido')
