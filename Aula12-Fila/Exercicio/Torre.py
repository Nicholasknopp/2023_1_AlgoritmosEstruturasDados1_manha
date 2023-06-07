from abc import ABCMeta, abstractmethod

class Torre(metaclass=ABCMeta):
    def __init__(self, id=int, nome=None, endereco=None):
        self.id = id
        self.nome = nome 
        self.ano = endereco
        
    def imprimir(self):
        print("id:" + self.id)
        print("Nome: " + self.nome)
        print("Endereço: " + str(self.endereco) )
        
    @abstractmethod
    def cadastrar(torre):
        id = int(input('Id: '))
        nome = str(input('Nome: '))
        endereco = str(input('Endereço: '))
        torre.append((id, nome, endereco))
        
    def imprimir(torre):
        id = int(input('Id: '))
        nome = str(input('Nome: '))
        endereco = str(input('Endereço: '))
        torre.append((id, nome, endereco))
    
        