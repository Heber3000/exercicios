from Ponto import Ponto
from Retangulo import Retangulo

ponto1 = Ponto(3,4)
ponto2 = Ponto(5,6)

print(ponto1.imprimir_coordenada_x_y())
print(ponto2.imprimir_coordenada_x_y())

ret1 = Retangulo(10,20)
ret2 = Retangulo(10,20)

print(ret1.mostrar_centro())
print(ret2.mostrar_centro())

print(ret1.area())
print(ret2.area())

