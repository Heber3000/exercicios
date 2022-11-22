class Carro:
    def __init__(self,motor,direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calculo_do_sentido(self):
        return self.direcao.valor

    def girar_direita(self):
        self.direcao.girar_direita()

    def girar_esquerda(self):
        self.direcao.girar_esquerda()





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


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'




class Direcao:
    rotacao_a_direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
                         }
    rotacao_a_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: OESTE
                         }




    def __init__(self):
        self.valor = NORTE


    def girar_direita(self):
       return  self.rotacao_a_direita[self.valor]


    def girar_esquerda(self):
        return self.rotacao_a_esquerda[self.valor]


print()

if __name__ == '__main__':
    direcao = Direcao()
    direcao.girar_direita()
    print(direcao.girar_direita())
