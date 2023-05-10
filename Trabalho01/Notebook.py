from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDebateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDebateria = tempoDebateria
       
    def getInformacoes(self):
        return super().getInformacoes() + "\nBateria: " + str(self.__tempoDebateria)
   
    def cadastrar(self):
        print("Modelo cadastrado")
        print("Tipo de cor cadastrado")
        print("Preço cadastrado ")
       
    def imprimir(self):
        print(self.cadastrar() )
        print( self.getInformacoes() )
       #print("Modelo: " + self.modelo)
       #print("cor: " + str(self.cor) )
       #print("Preço " + str(self.preco) )
        print("Tempo De Bateria " + str(self.__tempoDebateria))

