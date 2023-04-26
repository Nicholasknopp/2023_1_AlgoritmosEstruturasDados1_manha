from ContaBancaria import ContaBancaria

class Corrente(ContaBancaria):
    def __init__(self, conta=None, agencia=None, qtddisponivel=500):
        super().__init__(conta, agencia)
        self.disponivel = qtddisponivel
        
    def cadastrar(self):
        print("Conta cadastrar")
        
    def depositar(self):
        print("depositado")
        
    def imprimirEspecifico(self):
        super().imprimir()
        print("Disponivel: " + str(self.disponivel))