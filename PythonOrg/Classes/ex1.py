class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,cor):
        self.cor = cor

    def mostrarCor(self):
        return self.cor


if __name__ == '__main__':
    b= Bola
    b.trocaCor = 'verde'
    print(b.trocaCor)
