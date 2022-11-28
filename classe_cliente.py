#netflix

class Cliente:
    def __init__(self,nome,plano,email):
        self.nome = nome
        self.email = email
        lista_planos=['Básico','Padrão','Premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')


    def mudar_plano(self,plano):
        self.plano = plano



cliente = Cliente('Heber','Padrão','exemplo@gmail.com')
print(cliente.nome)