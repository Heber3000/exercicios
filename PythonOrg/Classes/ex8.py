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


    def mostrar_bucho(self):
        return f'{self.nome} comeu {self.bucho}'



    def digerir(self):
        print(f'\n{self.nome} digeriu a {self.bucho.pop()}')
        print(self.bucho)


if __name__ == '__main__':
    macaco1=Macaco('cesar')
    macaco2=Macaco('koba')



    macaco1.comer('banana')
    macaco1.comer('maça')
    macaco1.comer('uva')
    macaco1.comer(macaco2.nome)

    print(macaco1.mostrar_bucho())


    macaco2.comer('Pera')
    macaco2.comer('mandioca')
    macaco2.comer('batata')
























