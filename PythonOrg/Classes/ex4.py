class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        return self.idade + anos


    def emagrecer(self,peso_extra):
        return self.peso - peso_extra

    def engordar(self,peso_extra):
        return self.peso + peso_extra

    def crescer(self,anos):

        if self.idade <= 21:
            self.altura += 0.5*anos
            return self.altura


if __name__ == '__main__':
    heber = Pessoa('Heber',17,100,196)
    print(heber.emagrecer(5))
    print(heber.crescer(3))




