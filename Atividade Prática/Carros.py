from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca=None, modelo=None, qtdPortas=4):
        super().__init__(modelo)
        self.marca = marca
        self.__qtdPortas = qtdPortas
        self.proximo = None
        
    def __str__(self):
        texto  = "\n-------------------"
        texto += "\nMarca: " + self.marca
        texto += "\nModelo: " + self.modelo
        texto += "\nqtdPortas: " + str( self.__qtdPortas )
        return texto
        
    def imprimir(self):
        print("Marca: " + str(self.marca))
        print("Modelo: " + str(self.modelo))
        print("Portas: " + str(self.__qtdPortas))
        
    