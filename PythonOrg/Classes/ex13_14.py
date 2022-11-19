class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def nome(self,nome):
        self.nome = nome

    def retornar_nome(self):
        return self.nome

    def salario(self,salario):
        self.salario = salario

    def retornar_salario(self):
        return self.salario

    def aumenta_salario(self,aumento):
        self.salario +=aumento
        return self.salario


if __name__ == '__main__':
    robson = Funcionario('Robson',2000)
    print(robson.retornar_salario())
    print(robson.aumenta_salario(20))