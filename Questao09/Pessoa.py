from abc import ABCMeta, abstractmethod

class Pessoa(metaclass=ABCMeta):
    def __init__(self, Nome, Telefone):
        self.Nome = Nome
        self._Telefone = Telefone
    
    @abstractmethod                                                                                                             
    def marcarPresenca(self):
        print("Presenca")

    def imprimir(self):
        print("Nome: " + str(self.Nome))
        print("Telefone: " + str(self._Telefone) )

        
  