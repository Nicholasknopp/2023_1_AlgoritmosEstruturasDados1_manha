from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):
    def __init__(self, conta=None, agencia=None):
        self.conta = conta
        self.agencia = agencia
    
    @abstractmethod                                                                                                             
    def cadastrar(self):
        pass
    
    @abstractmethod
    def depositar(self):
        pass
        
    def imprimir(self):
        print("Conta: " + str( self.conta ))
        print("Agencia: " + str(self.agencia) )
        
    @abstractmethod
    def imprimirEspecifico(self):
        pass