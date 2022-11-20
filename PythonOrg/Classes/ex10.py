class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valor = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel


    def abatecer_valor(self,entrada_valor):
        self.entrada_valor = entrada_valor
        return f'{self.entrada_valor/self.valor} litros'


    def abastecer_litro(self,entrada_litro):
        self.entrada_litro = entrada_litro
        self.quantidadeCombustivel += self.entrada_litro
        return f'foi adicionado {self.entrada_litro} e agora  {self.quantidadeCombustivel} litros'

    def alterar_valor(self,valorLitro):
        self.valor = valorLitro

    def alterar_combustivel(self,tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterar_quantidade_de_combustivel(self,quantidadeCombustivel):
        self.tipoCombustivel = quantidadeCombustivel




if __name__ == '__main__':
    ex = BombaCombustivel('Gasolina',5,40)
    print(ex.abastecer_litro(50))
    print(ex.abatecer_valor(400))

