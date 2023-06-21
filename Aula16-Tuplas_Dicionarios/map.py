precos = [ 10 , 20, 30]

def aumentarPreco( p ):
    return p * 1.1

novosprecos = map( aumentarPreco , precos )

print( novosprecos )
print( list( novosprecos ))

valores = [(10,20) , (30, 40)]
def somar( x ):
    return x[0] + x[1]

somas = map( somar, valores )
print( list( somas ) )