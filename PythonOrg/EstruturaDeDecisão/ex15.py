lado_A= float(input('Informe o lado do triângulo: '))
lado_B= float(input('Informe outro lado do triângulo:'))
lado_C= float(input('Informe outro lado do triângulo:'))

if lado_A + lado_B < lado_C or lado_C+lado_A < lado_B:
    print('\nNão é triangulo')
else:
    print('\nÉ triângulo')
    if lado_A == lado_B and lado_A == lado_C:
        print('Equilátero')
    elif lado_A == lado_B or lado_A == lado_C or lado_C==lado_B:
        print('Isóceles')
    else:
        print('Escaleno')
