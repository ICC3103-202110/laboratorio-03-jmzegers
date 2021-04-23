from Coup import Coup
import time
from Carta import Carta
from Jugador import Jugador
import random



print("¡Bienvenido al juego de Coup!")

print("¿Cuantos jugadores van a participar?")
num_jugadores = int(input("Solo pueden tres o cuatro: "))

#Asegurarse de que solo puedan haber tres o cuatro jugadores
while (num_jugadores != 3 and num_jugadores != 4):
    print("Numero invalido")
    time.sleep(2)
    print("¿Cuantos jugadores van a participar?")
    num_jugadores = int(input("Solo pueden tres o cuatro: "))

i = 0
nombres_jugadores = []
while i < num_jugadores:
    nombre = input("Jugador " + str(i + 1) + " escriba su nombre: ")
    nombres_jugadores.append(nombre)
    i += 1

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
i = 0
jugadores = []
while i < num_jugadores:
    cartas_jug = []
    cartas_jug.append(mazo_barajado[0])
    cartas_jug.append(mazo_barajado[1])
    mazo_barajado.pop(0)
    mazo_barajado.pop(0)
    nombre = nombres_jugadores[i]
    jugador = Jugador(nombre, i + 1, 2, cartas_jug)
    jugadores.append(jugador)
    i += 1

print("Ahora vamos a mostrar las cartas de cada jugador")

print("")
#Mostrarle a cada jugador sus cartas
for j in jugadores:
    print("Cartas del jugador " + str(j.numero) + ":")
    print("Presione Enter para continuar")
    print("")
    for carta in j.cartas:
        print(carta.tipo)
    print("")
    input("Presione Enter para continuar")
    i = 1
    while i <= 40:
        print("")
        i += 1

#Aqui comienza el juego
Coup.Juego(jugadores, mazo_barajado)