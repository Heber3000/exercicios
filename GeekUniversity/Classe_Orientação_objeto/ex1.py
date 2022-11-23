class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def set_nome(self,nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_idade(self,idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_altura(self,altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def imprimir_dados(self):
        return f'Nome:{self.nome}\nidade:{self.idade}\naltura:{self.altura}'


nome = str(input("Informe o nome:")).title()
idade = int(input('informe a idade:'))
altura = float(input('Informe a altura'))

if __name__ == '__main__':
    pessoa = Pessoa(nome,idade,altura)
    print(pessoa.imprimir_dados())
