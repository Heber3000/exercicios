salarioBase = 200
vendedores = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
    valor_Vendas = float(input('Informe o total de vendas do vendedores:'))
    salarioTotal = salarioBase + valor_Vendas*9/100
    indice = int(salarioTotal/100) - 1
    if indice > 9:
        indice = 9
    elif indice  < 1:
        indice = 1
    print(indice)
    vendedores[indice-1] += 1

for i in range(0,9):
    print(f'\n{i*100+200}, {(i+1)*100 + 199}, {vendedores[i]}')
