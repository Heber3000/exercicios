
class TV:
    def __init__(self,canal,modelo:str,servico_streaming):
        self.canal = canal
        self.volume = 0
        self.modelo = modelo
        self.servico_streaming = servico_streaming

    def modelo(self,modelo):
        self.modelo = modelo

    def servico_streaming(self,opc):
        servico_streaming = {'Netflix':44.99,'Prime':12.99,'Hbo':29.00}
        return servico_streaming[opc]


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
        f'O modelo da tv {self.modelo}\nE o serviço presente {ser}'

class ControleRemoto(TV):
    pass










