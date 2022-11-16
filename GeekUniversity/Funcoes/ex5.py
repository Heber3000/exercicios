import math

def volume_esfera(raio):
    volume = math.pi * (4 / 3) * math.pow(raio, 3)

    return  f'O volume da esfera é {round(volume)}'

print(volume_esfera(5))