from Carros import Carro
from Drones import Drone
from Fila import Fila

c1 = Carro("Fiat", "Doblo", 5)
c2 = Carro("Renault", "Sandero", 4)

fila = Fila()
fila.add(c1)
fila.add(c2)
print(" ---------------------------")
fila.remover()
fila.remover()

d1 = Drone("DJI Mini 3 Pro.", "express", 4)
d2 = Drone("DJI Mavic Air 2S.", "Samsung", 2)

fila = Fila()
fila.add(d1)
fila.add(d2)
print(" ---------------------------")
fila.remover()
fila.remover()
