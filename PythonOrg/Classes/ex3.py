class Retangulo:
    def __init__(self,comprimento,altura):
        self.comprimento = comprimento
        self.altura = altura

    def mudar_comprimento(self,comprimento):
        self.comprimento = comprimento

    def mudar_altura(self,altura):
        self.comprimento = altura

    def retorno_comprimento(self):
        return self.comprimento

    def retorno_altura(self):
        return self.altura

    def calculo_area(self):
        return self.comprimento*self.altura



altura = float(input('Informe o lado maior do retangulo: '))
comprimento = float(input('Informe o lado maior do triangulo: '))

# supondo 1 metro quadrado 5 pisos
if __name__ == '__main__':
    r = Retangulo(altura,comprimento)
    print(f'A Quantidade de piso é {r.calculo_area()*5} ')
