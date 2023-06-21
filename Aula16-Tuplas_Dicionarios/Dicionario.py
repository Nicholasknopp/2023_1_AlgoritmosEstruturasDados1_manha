filho1 = {"nome" : "Júlia", "idade" : 14 }
filho2 = {"nome" : "Nicholas", "idade" : 21 }
filho3 = {"nome" : "Fernando", "idade" : 65 }

print( filho1 )
print( "Nome: ", filho1["nome"] )
print( filho1.keys() )
for chave, valor in filho1.items():
    print( chave, "-", valor)
    
for chave in filho1.keys():
    print( chave, "-", filho1[chave])
    
    
print("-------------")
prole = filho1, filho2
print( prole )
print( prole[0] )
#prole[0] = filho3
filho1["nome"] = "Juliana"
print( prole[0])