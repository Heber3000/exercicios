print('Equação do segundo grau ax2 + bx + c')
a = float(input('Informe um valor de a:'))

import math

if a == 0:
    print('Não é equação do segundo grau.')
else:
    b = float(input('Informe um valor b:'))
    c = float(input('Informe um valor c:'))
    delta = math.pow(b,2) - 4*a*c
    if delta < 0:
        print('Não há raízes')
    elif delta==0:
        print(f'Há apenas uma raiz {(-b+math.sqrt(delta))/2*a}')
    else:
        print(f'Há duas raízes {(-b+math.sqrt(delta))/2*a} e {(-b+math.sqrt(delta))/2*a}')
