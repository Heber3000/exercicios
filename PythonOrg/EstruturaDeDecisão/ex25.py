print('Responda as perguntas com S(sim) ou N(não):\n')

telefone = input('Voce telefonou para a vitima?').upper()
local = input('Esteve no local do crime ?').upper()
casa = input('Mora perto da vítima ?').upper()
divida = input('Devia para a vítima ?').upper()
trabalho = input('Já trabalhou com a vítima?').upper()
contador = 0

if telefone == 'S':
    contador += 1

if local == 'S':
    contador += 1

if casa == 'S':
    contador += 1

if divida == 'S':
    contador += 1

if trabalho == 'S':
    contador += 1

if contador <= 2:
    print('\nSuspeita')
elif contador <= 4:
    print('\nCúmplice')
else:
    print('\nAssassino')

