perguntas = {'Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?',
             'Já trabalhou com a vítima?'}

questionario = {}

for resposta in perguntas:
    questionario[resposta] = input('Responda S(SIM) ou N(não) %s' % resposta).upper()

contador = 0

for resposta in questionario.values():
    if resposta == 'S':
        contador += 1

if contador < 2:
    print('inocente')
elif contador <= 2:
    print('suspeita')
elif contador <= 4:
    print('suspeita')
else:
    print('culpado')