hora_trabalho = float(input('Informe o valor da hora por trabalho:'))
total_hora_trabalhadas = float(input('Informe o total de horas trabalhadas:'))

print(f'\nO salário bruto R${hora_trabalho*total_hora_trabalhadas}')
print(f'O valor descontado do imposto de renda(11%) R${(hora_trabalho*total_hora_trabalhadas)*0.11}')
print(f'O valor pago ao INSS(8%) {(hora_trabalho*total_hora_trabalhadas)*0.08}')
print(f'O valor do sindicato(5%) é R$ {(hora_trabalho*total_hora_trabalhadas)*0.05}')
descontos = (hora_trabalho*total_hora_trabalhadas)*0.11 + (hora_trabalho*total_hora_trabalhadas)*0.08 + (hora_trabalho*total_hora_trabalhadas)*0.05
print(f'O salário liguido é {(hora_trabalho*total_hora_trabalhadas) - (descontos)}')