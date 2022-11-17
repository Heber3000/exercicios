class ContaCorrente:
    def __init__(self,nome:str,numerodaconta:int,saldo:float):
        self.nome = nome
        self.numerodaconta = numerodaconta
        self.saldo = 0


    def alterarNome(self,nome):
        self.nome = nome

    def deposito(self,entrada):
        self.saldo += entrada


        return f'O saldo é R${self.saldo}'

    def saque(self,saida):
        self.saldo -= saida
        return f'O saldo é R${self.saldo}'



if __name__ == '__main__':
    patrick = ContaCorrente('Patrick ',1900,0)
    print(patrick.alterarNome('Patrick Aloe'))
    print(patrick.deposito(20))
    print(patrick.saque(20))



