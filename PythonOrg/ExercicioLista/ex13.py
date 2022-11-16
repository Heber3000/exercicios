meses = ('1-Janeiro','2-Fevereiro','3-Março','4-Abril','5-Maio','6-Junho','7-Julho','8-Agosto'
               ,'9-Setembro','10-Outubro','11-Novembro','12-Dezembro')

temperaturas = {}

for resposta_temperatura in meses:
    temperaturas[resposta_temperatura] = float(input('Informe a tempera do mês %s:' % resposta_temperatura))

somaTemp = 0

for valor in temperaturas.values():
    somaTemp += valor

media = somaTemp/12

print(f'a media de temperatura é {"%.2f" % media}\nAs temperaturas com média:')

for mes in meses:
    if temperaturas[mes] > media:
        print(f'{mes},{temperaturas[mes]}')
    