class Retangulo:
    def __init__(self,largura,altura,centro):
        self.largura = largura
        self.altura = altura
        self.centro = centro

    def imprimir(self):
        return self.largura, self.altura

    def area(self):
        return self.largura*self.altura

    def mostrar_centro(self):
        return self.centro

