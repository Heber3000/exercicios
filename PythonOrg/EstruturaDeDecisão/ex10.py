periodo = input('Informe qual período você estuda (M-matutino ou V-Vespertino ou N- Noturno):').upper()

if periodo == 'M':
    print('Bom Dia')
elif periodo == 'V':
    print('Boa Tarde')
elif periodo == 'N':
    print('Boa Noite')
else:
    print('Valor Inválido')
