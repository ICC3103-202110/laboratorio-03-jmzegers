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





#Comienzo del juego
turno = 1
a = True
while a == True:
    #Indicar a que jugador le toca jugar
    for j in jugadores:
        if j.numero == turno:
            jugador_turno = j
    
    print(jugador_turno.nombre, + ", le toca jugar")
    
    
    
    accion = str(input("""¿Que accion quiere tomar?
                   Recibir ingreso [I] 
                   Pedir ayuda externa [E]
                   Hacer un golpe [C] (Cuesta 7 monedas)
                   Duque: Cobrar impuestos [T] 
                   Asesino: Asesinar [A] (Cuesta tres monedas)
                   Embajador: Intercambiar [X]
                   Capitan: Robar [S]
    """)).capitalize()
    
    #El jugador toma la accion de Recibir Ingreso
    if accion == "I":
        jugador_turno.num_monedas += 1
    
    #El jugador toma la accion de Ayuda Externa
    elif accion == "E":
        jugador_turno.num_monedas += 2
        
    #El jugador toma la accion de Hacer un Golpe
    elif accion == "C":
        if jugador_turno.num_monedas < 7:
            print("No tiene suficientes monedas")
        else:
            print(accion)
    
    #El jugador toma la accion de Cobrar Impuestos
    elif accion == "T":
        jugador_turno.num_monedas += 3
    
    #El jugador toma la accion de Asesinar
    elif accion == "A":
        if jugador_turno.num_monedas < 3:
            print("No tiene suficientes monedas")
        else:
            #Asesinar
            print(accion)
    
    #El jugador toma la accion de Intercambiar
    elif accion == "X":
        print("Elija la carta que quiere intercambiar")
        i = 1
        for carta in jugador_turno.cartas:
            print(carta.tipo, "[" + i + "]")
            i += 1
        num_carta = int(input("Numero de la carta: "))
        carta_a_descartar = jugador_turno.cartas(num_carta - 1)
        mazo_barajado.append(carta_a_descartar)
        jugador_turno.cartas.pop(num_carta)
        jugador_turno.cartas.append(mazo_barajado[0])
    
    #El jugador toma la accion de Robar
    elif accion == "S":
        for j in jugadores:
            if (j != jugador_turno):
                print(j.nombre)
        print(" ")
        nombre_elegido = input("Elija al jugador al que quiera robar: ").capitalize()
        for j in jugadores:
            if j.nombre == nombre_elegido:
                if j.num_monedas <= 2:
                    j.num_monedas -= 2
                else:
                    j.num_monedas = 0
    
    
    
    
    
    if (turno == 3):
        turno = 0
    turno += 1







