from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.proximo = nodo
            nodo.anterior = self.fim
            self.fim = nodo
        self.tamanho += 1
        self.imprimir()
        
    def imprimir( self):
        print("--------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho) )
            
    def imprimirReverso( self):
        print("--------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho) )
            
            
    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho = 0
        else:
            anterior = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            self.tamanho -= 1
            self.imprimir()
                
            
        
        
        
        
        
        
        
        
        
        
        
    
          
                