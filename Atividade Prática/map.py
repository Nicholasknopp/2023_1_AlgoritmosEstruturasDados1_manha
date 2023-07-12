# Esta função map vai multiplicar os numeros por 10 e depois vai dividir os numeros por 2.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculo = list(map(lambda x: x*10/2, numeros))
print(calculo)