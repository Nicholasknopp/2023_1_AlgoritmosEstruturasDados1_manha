from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
        
    def getInformacoes(self):
        return super().getInformacoes() + "\nPotência: " + self._potenciaDaFonte
    
    def cadastrar(self, modelo, cor, preco):
        print("Modelo cadastrado")
        print("Cor cadastrado")
        print("Preço cadastrado ")
        
    def imprimir(self):
        print("Modelo: " + self.modelo)
        print("cor: " + str(self.cor) )
        print("Preço " + str(self.preco) )
        print("Potência Da Fonte " + str(self._potenciaDaFonte))
    
    