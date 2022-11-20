class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura


    def imprimir(self):
        return self.largura, self.altura

    def area(self):
        return self.largura*self.altura

    def mostrar_centro(self):
        return self.largura/2,self.altura/2

