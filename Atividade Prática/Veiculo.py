from abc import ABCMeta

class Veiculo(metaclass=ABCMeta):
    def __init__(self, modelo=None):
        self.modelo = modelo 
        
    def imprimir(self):
        print("Modelo: " + self.modelo)
        
