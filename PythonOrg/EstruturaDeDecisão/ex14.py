nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
media = (nota1+nota2)/2
print('')
conceito = str
if media > 10:
    print('Nota não pode ser maior que 10')
else:
    if media <= 9 or media <= 10:
        conceito = 'A'
    elif media <= 7.5:
        conceito = 'B'
    elif media <= 6:
        conceito = 'C'
    elif media <= 4:
        conceito = 'D'
    else:
        conceito = 'E'

    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        print('Aprovado')
    else:
        print('Reprovado')



