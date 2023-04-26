from ContaBancaria import ContaBancaria

class Poupanca(ContaBancaria):
    def __init__(self, conta=None, agencia=None, valcartao=4):
        super().__init__(conta, agencia)
        self.valcartao = valcartao
        
    def cadastrar(self):
        print("Conta cadastrar")
        
    def depositar(self):
        print("depositado")
        
        
    def imprimirEspecifico(self):
        super().imprimir()
        print("Cartão: " + str(self.valcartao))
        