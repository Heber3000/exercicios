salario = float(input('Informe o salário:'))

if salario <= 280:
    reajuste = 1.2
elif salario < 280 or salario < 700:
    reajuste = 1.17
elif salario < 700 or salario < 1500:
    reajuste = 1.1
else:
    reajuste = 1.05

print(f'O salarío antes do reajuste R${salario}\nO percentual de aumento foi de {round((reajuste - 1)*100)}%'
      f'\nO Valor do aumento R${salario*reajuste - salario}\nO novo salário é R${salario*reajuste}')