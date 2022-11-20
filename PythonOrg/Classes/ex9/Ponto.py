class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def imprimir_coordenada_x_y(self):
        return self.x, self.y

    def ponto_medio(self):
        return (self.x + self.y)/2


