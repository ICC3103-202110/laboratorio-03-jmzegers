import time
from Carta import Carta
from Jugador import Jugador
import random

print("¡Bienvenido al juego de Coup!")

print("¿Cuantos jugadores van a participar?")
num_jugadores = int(input("Solo pueden tres o cuatro: "))

while (num_jugadores != 3 and num_jugadores != 4):
    print("Numero invalido")
    time.sleep(2)
    print("¿Cuantos jugadores van a participar?")
    num_jugadores = int(input("Solo pueden tres o cuatro: "))

lista = []
lista.append("Duque")
lista.append("Asesino")
lista.append("Capitan")
lista.append("Embajador")
lista.append("Condesa")

#Aqui creo el mazo
mazo = []
for c in lista:
    i = 1
    while (i <= 3):
        c1 = Carta(c)
        mazo.append(c1)
        i += 1
        
#Barajar las cartas
mazo_barajado = []
i = len(mazo) - 1
while i >= 0:
    lugar_azar = random.randint(0, i)
    carta_azar = mazo[lugar_azar]
    mazo_barajado.append(carta_azar)
    mazo.pop(lugar_azar)
    i -= 1

#Se reparten dos cartas a cada jugador
i = 1
jugadores = []
while i <= num_jugadores:
    cartas_jug = []
    cartas_jug.append(mazo_barajado[0])
    cartas_jug.append(mazo_barajado[1])
    mazo_barajado.pop(0)
    mazo_barajado.pop(0)
    jugador = Jugador("a", i, cartas_jug)
    jugadores.append(jugador)
    i += 1

turno = 1
a = True
while a == True:
    #Indicar a que jugador le toca jugar
    for j in jugadores:
        if j.numero == turno:
            jugador_turno = j
    print(jugador_turno.nombre, + ", le toca jugar")
    accion = input("""¿Que accion quiere tomar?
                   Recibir ingreso [a]
                   Pedir ayuda externa
                   Hacer un golpe []
                   Duque: Cobrar impuestos [c]
                   Asesino: Asesinar [ass]
                   Embajador: Intercambiar
                   Capitan: Robar
    """)
    if (turno == 3):
        turno = 0
    turno += 1






