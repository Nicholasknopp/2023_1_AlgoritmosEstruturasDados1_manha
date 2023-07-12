from Carros import Carro

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
    
    def add(self, carro):
        if self.primeiro == None:
            self.primeiro = carro
            self.ultimo = carro
        else:
            self.ultimo.proximo = carro
            self.ultimo = carro
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        print("---------------------")
        if self.primeiro == None:
            print("Fila Vazia!")
        else:
            aux = self.primeiro
            while aux :
                print( aux )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))
  
            
    def remover(self):
        aux = self.primeiro
        if self.primeiro == None:
            print("Fila Vazia!")  
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir() 
        if aux is not None: 
            aux.proximo = None 
        return aux
                
            
        
        
        
        
        
        
        
        
        
        
        
    
          
                