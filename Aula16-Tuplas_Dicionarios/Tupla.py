jogadores = "João", "Maria", "José", "Júlia"

print( jogadores )
print( jogadores[1] )
print( jogadores[1:3] )
print( jogadores[1:-1] )
selecionados = jogadores[2:] , jogadores[0]
print( jogadores[1:2] )
print("---------------------------------")
print( jogadores[2:] , jogadores[0])
#print( jogadores[ :2:-1] )

def calcular(x, y):
    return x+y, x-y, x*y, x/y

resultado = calcular( 10, 5 )
print( resultado )
print( "Multiplicação:", resultado[2])
a, b, c, d = calcular( 9, 3)
print("soma", a)
print("subtração", b)
print("Multiplicação", c)
print("Divisão", d)