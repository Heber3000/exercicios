import math


def quadradoPerfeito(num):
    if num <= 0:
        return f'O {num} é invalido(não pode ser negativo)'
    raiz_quadrada = math.sqrt(num)
    if raiz_quadrada == int(raiz_quadrada):
        return f'O {num} é um quadrado perfeito de {int(raiz_quadrada)}'
    else:
        return f'O {num} Não é quadrado perfeito'



print(quadradoPerfeito(4))
