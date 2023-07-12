from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca=None, modelo=None, qtdhelices=4):
        super().__init__(modelo)
        self.marca = marca
        self._qtdhelices = qtdhelices
        self.proximo = None
    
    def __str__(self):
        texto  = "\n-------------------"
        texto += "\nMarca: " + self.marca
        texto += "\nModelo: " + self.modelo
        texto += "\nqtdHélices: " + str( self._qtdhelices )
        return texto
        
    def imprimir(self):
        print("Marca: " + str(self.marca))
        print("Modelo" + str(self.modelo))
        print("Hélices: " + str(self._qtdhelices))
    