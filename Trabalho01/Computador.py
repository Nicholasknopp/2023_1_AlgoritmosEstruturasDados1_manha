from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        a = "Modelo: " + self.modelo + "\nCor: " + self.cor + "\nPreço: " + str(self.preco)
        return a
    
    @abstractmethod
    def cadastrar(self, modelo, cor, preco):
        pass
    
    def imprimir(self):
        print("Modelo: " + self.modelo)
        print("cor: " + str(self.cor) )
        print("Preço " + str(self.preco) )