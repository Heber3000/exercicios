class Tv:
    def __init__(self,numero_canal,volume):
        self.numero_canal = numero_canal
        self.volume = volume

    def mudar_canal(self,numero_canal):
        self.numero_canal = numero_canal

        if self.numero_canal > 100 or self.numero_canal < 0:
            return f'Não há numero de canal de menor que 0 e maior que 100'
        else:
            return f'Número do canal {self.numero_canal}'

    def aumentar_volume(self,entrada):
        self.volume += entrada
        if self.volume >= 75:
            return f'O volume acima de 75 implica em perdas auditivas'
        else:
            return f'{self.volume}'

    def diminuir_volume(self, entrada):
        self.volume += entrada
        if self.volume <= 0:
            return f'Não pode ser negativo'
        else:
            return f'{self.volume}'


if __name__ == '__main__':
    ex = Tv(4,0)

    print(ex.mudar_canal(6))
    print(ex.aumentar_volume(50))
    print(ex.diminuir_volume(-100))








