class Macaco:
    def __init__(self,nome:str):
        self.nome = nome
        self.bucho = []

    def nome(self,nome):
        self.nome = nome

    def retornar_nome(self):
        return self.nome

    def comer(self,alimentos):
        self.bucho.append(alimentos)


    def bucho(self):
        return f'\n{self.nome}:{self.bucho}'

    def digerir(self):
        print(f'\n{self.nome}:{self.bucho.pop()}')


if __name__ == '__main__':
    macaco1=Macaco('cesar')
    macaco2=Macaco('koba')



    macaco1.comer('banana')
    macaco1.comer('maça')
    macaco1.comer('uva')

    print(macaco1.digerir())

    macaco2.comer('Pera')
    macaco2.comer('mandioca')
    macaco2.comer('batata')

    print(macaco1.bucho)






















