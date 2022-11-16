hora_por_trabalho=float(input('Informe o valor da hora por trabalho:'))
total_de_horas_trabalhadas = float(input('Informe o total de horas trabalhadas'))
salario_bruto = hora_por_trabalho*total_de_horas_trabalhadas

if salario_bruto < 900:
    desconto = 0
elif salario_bruto <= 1500:
    desconto = 0.05
elif salario_bruto <= 2500:
    desconto = 0.1
else:
    desconto = 0.2

print(f'\nSalário Bruto:{"%.1f" % hora_por_trabalho}x{"%.1f" % total_de_horas_trabalhadas}:                                        R$:{salario_bruto}')
print(f'IR({desconto*100})%:                                                       :R$:{salario_bruto*desconto}')
print(f'INSS(10%):                                                      :R$:{salario_bruto*0.1}')
print(f'FGTS(11%):                                                      :R$:{salario_bruto*0.11}')
print(f'Total de Descontos                                              :R$:{salario_bruto*desconto+salario_bruto*0.1+salario_bruto*0.11}')
print(f'Salário Bruto:                                                  :R$:{salario_bruto-(salario_bruto*desconto+salario_bruto*0.1+salario_bruto*0.11)}')

