salario = 1000
contador = 0


print(f'R${"%2.f" % float(salario)}.00|1995')

for i in range(1996,2022+1):
    contador +=1
    print(f'R${"%.2f" % float(salario*(1 + 0.015*contador))}|Periodo {i}')

