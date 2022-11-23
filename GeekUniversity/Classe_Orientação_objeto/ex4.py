class Tv:
    def __init__(self,modelo,controle):
        self.modelo = modelo
        self.controle = controle

    def set_modelo(self,modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def aumentar_volume(self):
         self.controle.aumentar_volume()

    def diminuir_volume(self):
        self.controle.diminuir_volume()

    def mudar_canal(self):
        return self.controle.mudar_de_canal

    def aumentar_canal(self):
        self.controle.aumentar_numero_canal()

    def diminuir_canal(self):
        self.controle.diminuir_numero_canal()








class ControleRemoto:
    def __init__(self,canal,volume = 0):
        self.canal = canal
        self.volume = volume
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





    print(ex.consulta)



