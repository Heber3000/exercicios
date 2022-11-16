hora = float(input('Informe o quanto é ganho por hora:'))
total_horas_mes = float(input('Informe o total de horas de trabalhadas:'))

salario = hora*total_horas_mes

print(f'\nO total de salário ganho R${"%.2f" % salario}')