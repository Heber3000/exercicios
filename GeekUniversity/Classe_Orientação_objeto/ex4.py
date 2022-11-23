class Tv:
    def __init__(self,modelo,canal,volume):
        self.modelo = modelo
        self.canal = canal
        self.volume = volume

    def set_modelo(self,modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def aumentar_volume(self):
         self.volume.aumentar_volume()

    def diminuir_volume(self):
        self.volume.diminuir_volume()

    def mudar_canal(self):
        return self.canal.mudar_de_canal

    def aumentar_canal(self):
        self.canal.aumentar_numero_canal()

    def diminuir_canal(self):
        self.canal.diminuir_numero_canal()

    def consulta(self):
        return f'Modelo:{self.modelo}\nCanal:{self.canal}\nVolume:{self.volume}'







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


if __name__ == '__main__':
    ex = Tv('TCL',5,0)
    ex.aumentar_volume()
    print(ex.consulta())



