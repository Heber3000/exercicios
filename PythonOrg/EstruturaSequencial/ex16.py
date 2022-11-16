metros_quadrados_por_tinta = float(input('Informe a quantidade de metros quadrado pintadas: '))
quantidade_litros = metros_quadrados_por_tinta/3
latas_de_tintas = quantidade_litros/18


print(f'A Quantidade de latas de tintas é { round(latas_de_tintas)} e o preço a ser pago R${round(latas_de_tintas*80)}')