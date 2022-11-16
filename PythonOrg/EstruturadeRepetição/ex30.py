print('Preço do Pão: R$: 0.18')
contador = 0
for i in range(1,51):
    contador +=1
    print(f'{i} - {"%.2f" % float(contador*0.18)}')