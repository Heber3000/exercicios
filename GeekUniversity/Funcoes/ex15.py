def selecao_triangulo(lado_A,lado_B,lado_C):
    if lado_A+lado_B<lado_C or lado_A+lado_C <lado_B or lado_C+lado_B< lado_A:
        print('\nNão é triângulo')
    else:
        print('\nÉ Triângulo')
        if lado_A == lado_B and lado_A == lado_C:
            print('\nEquilatero')
        elif lado_A == lado_B or lado_C== lado_A or lado_C == lado_B:
            print('\nIsóceles')
        else:
            print('\nEscaleno')
    return ''


print(selecao_triangulo(2,4,3))



