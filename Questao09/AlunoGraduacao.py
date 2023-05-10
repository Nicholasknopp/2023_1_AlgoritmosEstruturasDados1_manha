from Pessoa import Pessoa

class AlunoGraduacao:
    def __init__(self, Nome, Telefone, Matricula, Presencas):
        super().__init__(Nome, Telefone)
        self.__Matricula = Matricula
        self.Presencas = Presencas
        
    def getInformacoes(self):
        return super().getInformacoes() + "\nMatricula: " + str(self.__Matricula)
    
    def getMatricula(self):
        return self.__Matricula
    
    def setMatricula(self, Matricula):
        self.__Matricula = Matricula
    
        
    def imprimirEspecifico(self):
        print( self.getInformacoes() )
        print("Matricula: " + str(self.Matricula))
        print("Presencas: ", self.Presencas)