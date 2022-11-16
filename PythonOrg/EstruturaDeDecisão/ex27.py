total_morangos = float(input('Informe a quantidade de morangos:'))
total_macas = float(input('Informe a quantidade de maças:'))

if total_morangos <= 5:
    valor_morangos = total_morangos*2.2
else:
    valor_morangos = total_morangos*2.5

if total_macas <= 5:
    valor_macas = total_macas*1.8
else:
    valor_macas = total_morangos*1.5

total_frutas = total_morangos+total_macas
valor_bruto = valor_macas+valor_morangos

desconto = 0
if total_frutas > 8 or valor_bruto>25:
    desconto += 0.9
    valor_bruto = valor_bruto*desconto

print(f'O valor a ser pago R${valor_bruto} o total de frutas {total_frutas}kg')

