from Torre import Torre

class Apartamento(Torre):
    def __init__(self, id=int, numero=None, torre=None, vaga=int, proximo=None):
        super().__init__(id)
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        proximo = proximo
        
    def imprimirEspecifico(self):
        super().imprimir()
        print("Portas: " + str(self.qtdPortas))