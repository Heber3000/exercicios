
class Motor:
    def __init__(self,velocidade):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 2:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -=1


# Testando Motor
if __name__ == '__main__':
    motor = Motor(0)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)




class Direcao:
    def __init__(self,valor):
        self.valor = valor


    def girar_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        else:
            self.valor = 'Norte'


    def girar_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        else:
            self.valor = 'Norte'

print()

if __name__ == '__main__':
    direcao = Direcao('Norte')
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)