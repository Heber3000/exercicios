
class Quadrado:

    def __init__(self,lado):
        self.lado = lado


    def valor_lado(self,lado):
        self.lado = lado


    def retornar_lado(self):
        return self.lado

    def calculoArea(self):
        return self.lado*self.lado


if __name__ == '__main__':
    q = Quadrado(5)
    print(q.calculoArea())
    q.valor_lado(4)
    print(q.calculoArea())

