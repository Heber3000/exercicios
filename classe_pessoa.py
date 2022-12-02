class Pessoa:
    olhos = 2
    def __init__(self,nome:str,idade:int):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Muito Prazer meu nome é {self.nome}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pessoa=super().cumprimentar()
        return f'Coé,{cumprimentar_da_classe_pessoa}, aperto de mão'
    pass


class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pessoa=super().cumprimentar()
        return f'{cumprimentar_da_classe_pessoa}, beijo no rosto'

if __name__ == '__main__':
    paulo = Homem('Paulo',20)
    print(paulo.cumprimentar())
    rosa = Mulher('Rosa',23)
    print(rosa.cumprimentar())



