from ContaCorrente import Corrente

from ContaPoupanca import Poupanca

B = Corrente(1233, "Bradesco")
B.imprimir()
print("---------------------")
B.imprimirEspecifico()

C = Poupanca(3312, "Banrisul" )
C.imprimir()
print("---------------------")
C.imprimirEspecifico()

