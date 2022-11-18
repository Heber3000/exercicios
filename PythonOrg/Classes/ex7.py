class Tamagushi:

    def __init__(self,nome:str,fome,idade):
        self.nome = nome
        self.fome = fome
        self.idade = idade
        self.saude = 100


    def nome(self,nome):
        self.nome = nome

    def retornar_nome(self):
        return self.nome

    def fome(self,fome):
        self.fome = fome


    def retornar_fome(self):
        if self.fome > 50:
            return f'Indice de fome alto. Alimente ele'
        else:
            return f'Indice de fome baixo.'



    def idade(self,idade):
        self.idade = idade

    def retornar_idade(self):
        return self.idade

    def saude(self,perda):
        self.saude -= perda


    def retornar_saude(self):

        if self.saude <= 25:
            return f'saude Baixa'
        elif self.saude <= 50:
            return f'saúde média'
        else:
            return f'saúde normal'


    def humor(self):
        if self.fome * self.saude > 100:
            return f'feliz'
        else:
            return f'triste'





if __name__ == '__main__':
    robson = Tamagushi('Robson',10,2)
    robson.nome = 'Corasini'
    print(robson.retornar_nome())
    robson.fome = 90
    print(robson.retornar_fome())
    robson.saude = 100
    print(robson.retornar_saude())
    print(robson.humor())












