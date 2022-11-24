
class TV:
    def __init__(self,canal,modelo:str):
        self.canal = canal
        self.volume = 0
        self.modelo = modelo


    def modelo(self,modelo):
        self.modelo = modelo


    # Volume
    def aumentar_volume(self):
        self.volume +=1

    def diminuir_volume(self):
        self.volume -=1
    # Canal
    def mudar_de_canal(self,canal):
        self.canal = canal

    def aumentar_numero_canal(self):
        self.canal += 1

    def diminuir_numero_canal(self):
        self.canal -= 1

    # Consulta
    def consulta(self):
        return f'Canal:{self.canal}\nvolume{self.volume}'

    def consulta_modelo(self):
        return f'O modelo é {self.modelo}'


class ControleRemoto(TV):
    pass


if __name__ == '__main__':
    controle = ControleRemoto(5,'TCL')










