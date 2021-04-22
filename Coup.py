import time
from Carta import Carta
from Jugador import Jugador
import random

#Funcion para dudar si un jugador posee una cierta carta
def Duda (accion, jugador_turno, jugador_duda):
    s=False
    j=0
    nombre_carta = "a"
    if accion == "T":
        nombre_carta = "Duque"
    elif accion == "A":
        nombre_carta = "Embajador"
    elif accion == "S":
        nombre_carta = "Capitan"
    while j<len(jugador_turno.cartas):
        if jugador_turno.cartas[j].tipo == nombre_carta:
            s=True
        j+=1
    if s==True:
        carta_perdida=int(input(jugador_turno.nombre + " si tiene la carta "  + nombre_carta + "elije que carta perder 1/2"))-1
        jugador_duda.cartas.pop(carta_perdida)
    else:
        carta_perdida=int(input(jugador_turno.nombre + " no tiene la carta " + nombre_carta + " elije que carta perder 1/2"))-1
        jugador_turno.cartas.pop(carta_perdida)
    
def Neutralizacion (accion):
    #Jugador que se opone
    j=1
    print("que jugador es :")
    for i in jugadores:
        print("para jugador: " + i.nombre + " escriba " + str(j))
        j+=1
    jugador_duda=int(input())
    j = 0
    while j < len(jugadores):
        if j == jugador_duda - 1:
            jugador_acusa = jugadores[j]
        j += 1
    #Solo se pueden neutralizar:
        #1. Ayuda Extranjera (E)
        #2. Asesinato (A)
        #3. Robo (S)
    if accion == "E":
        print("La Ayuda Extranjera ha sido neutralizada!")
    elif accion == "A":
        print("El Asesinato ha sido neutralizado!")
    elif accion == "S":
        print("El Robo ha sido neutralizado!")
    return jugador_acusa

#Funcion para dudar una Neutralizacion
def Duda_Neutralizacion (accion, jugador_turno, jugador_acusa):
    tiene_carta = False
    nombre_carta2 = "a"
    if accion == "E":
        nombre_carta = "Duque"
    elif accion == "A":
        nombre_carta = "Condesa"
    elif accion == "S":
        nombre_carta = "Embajador"
        nombre_carta2 = "Capitan"
    for c in jugador_turno.cartas:
        if c.tipo == nombre_carta or c.tipo == nombre_carta2:
            tiene_carta = True
    if tiene_carta == True:
        print(jugador_turno + " tiene la carta adecuada!")
    

def Scanner_Respuestas (respuestas_validas, respuesta):
    while respuesta not in respuestas_validas:
        print("Respuesta invalida")



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
    print("Cartas del jugador " + j.numero + ":")
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




class Coup:
    def Juego(jugadores):
          jugadores = jugadores
        
          #Comienzo del juego
          turno = 1
          a = True
          while a == True:
              #Indicar a que jugador le toca jugar
                for j in jugadores:
                    if j.numero == turno:
                       jugador_turno = j
                print("")
                print("")
                print(jugador_turno.nombre + ", le toca jugar")
                input("Presione Enter para continuar")
                
                print("Monedas de cada jugador: ")
                for j in jugadores:
                    print(j.nombre + ":" + str(j.num_monedas))
                    
                print(" ")
                
                #Imprimo en consola las cartas que el jugador tiene en mano
                #y su descripcion.
                print("Cartas del jugador")
                for carta in jugador_turno.cartas:
                    print(carta.tipo)
                
                input("Presione Enter para continuar")
                
                #Aclaro la consola para que los otros jugadores no puedan
                #ver las cartas del que esta jugando
                i = 1
                while i <= 40:
                    print("")
                    i += 1
                
               
                    
                print("Monedas de cada jugador:")
                for j in jugadores:
                    print(j.nombre + ": " + str(j.num_monedas))
                
                print("")
                
                #Descripcion de cada carta (opcional)
                r = str(input("¿Desea ver la descripcion de cada carta? [S/N] ")).capitalize()
                if r == "S":
                    a = True
                    while a == True:
                        carta_a_desc = str(input("""¿Que carta quiere revisar?
                                                  Duque [D]
                                                  Asesino [A]
                                                  Embajador [E]
                                                  Capitan [C]
                                                  Condesa [S]""")).capitalize()
                        #Duque
                        if carta_a_desc == "D":
                            print("Puede tomar la accion de Cobrar Impuestos")
                            print("Esto significa que recibe tres monedas")
                            print("Tambien puede bloquear la accion de Ayuda Extranjera")
                        #Asesino
                        elif carta_a_desc == "A":
                            print("Puede Asesinar a una de las cartas de otro jugador")
                            print("Esto cuesta tres monedas")
                        #Embajador
                        elif carta_a_desc == "E":
                            print("Puede hacer un Intercambio")
                            print("Esto significa que puede cambiar las dos cartas que tiene actualmente")
                            print("Despues de esto, saca cuatro cartas del mazo y elige dos")
                            print("Tambien puede bloquear la accion de Robo")
                        #Capitan
                        elif carta_a_desc == "C":
                            print("Puede cometer un Robo")
                            print("Lo que significa robarle un maximo de dos monedas")
                            print("a eleccion")
                            print("Tambien puede bloquear la accion de Robo")
                        #Condesa
                        elif carta_a_desc == "S":
                            print("Esta carta solo sirve para bloquear un Asesinato")
                        
                        time.sleep(2.5)
                        r = str(input("¿Desea ver otra descripcion? [S/N]")).capitalize()
                        if r == "N":
                            break
                        
                
                print("")
                puede_realizar="n"
                while puede_realizar=="n":    
                    accion = str(input("""¿Que accion quiere tomar?
                                Recibir ingreso [I] 
                                Pedir ayuda externa [E]
                                Hacer un golpe [C] (Cuesta 7 monedas)
                                Duque: Cobrar impuestos [T] 
                                Asesino: Asesinar [A] (Cuesta 3 monedas)
                                Embajador: Intercambiar [X]
                                Capitan: Robar [S]
                    """)).capitalize()
                    acciones_posibles = ["I", "E", "C", "T", "A", "X", "S"]
                    while accion not in acciones_posibles:
                        print("Respuesta invalida")
                        accion = str(input("""¿Que accion quiere tomar?
                                Recibir ingreso [I] 
                                Pedir ayuda externa [E]
                                Hacer un golpe [C] (Cuesta 7 monedas)
                                Duque: Cobrar impuestos [T] 
                                Asesino: Asesinar [A] (Cuesta 3 monedas)
                                Embajador: Intercambiar [X]
                                Capitan: Robar [S]
                    """)).capitalize()
                    
                    if accion == "C":
                        if jugador_turno.num_monedas < 7:
                            print("No tiene suficientes monedas")
                        else:
                            puede_realizar="s"
                            
                        
                    elif accion == "A":
                        if jugador_turno.num_monedas < 3:
                            print("No tiene suficientes monedas")
                        else:
                            puede_realizar="s"
                    
                    else:
                        puede_realizar="s"
                    
                
                
                
                #El jugador toma la accion de Recibir Ingreso
                #Esta accion no puede ser bloqueada
                if accion == "I":
                    jugador_turno.num_monedas += 1
                
                #El jugador toma la accion de Ayuda Externa
                #Esta accion puede ser bloqueada
                #por un jugador que tenga la carta de Duque
                elif accion == "E":
                    r = input("¿Alguien quiere usar una Neutralizacion en contra de "  + jugador_turno.nombre + "? [S/N]").capitalize()
                    if r == "S":
                        jug_neutralizador = Neutralizacion("E")
                    else:
                        jugador_turno.num_monedas += 2
                    
                #El jugador toma la accion de Hacer un Golpe
                elif accion == "C":
                    print("a quien desea hacer el golpe?")
                    j=0
                    for i in jugadores:
                        print("para jugador: " + i.nombre + "escriba " + str(j))
                        j+=1
                    golpe=int(input())
                    carta_perdida=int(input("te hicieron un golpe "+golpe.nombre+" elije que carta perder 1/2"))-1
                    golpe.nombre.cartas.pop(carta_perdida)
                
                #El jugador toma la accion de Cobrar Impuestos
                elif accion == "T":
                    jugador_turno.num_monedas += 3
                
                #El jugador toma la accion de Asesinar
                elif accion == "A":
                    
                    
                    jugador_turno.num_monedas -= 3
                    r = input("¿Alguien quiere usar una Neutralizacion en contra de "  + jugador_turno.nombre + "? [S/N]").capitalize()
                    if r == "S":
                        jug_neutralizador = Neutralizacion("A")
                        r = input("""¿Alguien duda la Neutralizacion de """ +
                                  jug_neutralizador.nombre + """? [S/N]""").capitalize()
                        
                    else:
                        #El asesinato
                        #Asesinar
                        print("a quien desea asesinar?")
                        j=0
                        for i in jugadores:
                            print("para jugador: " + i.nombre + " escriba " + str(j + 1))
                            j+=1
                        asesinato=int(input()) - 1
                        if len(jugador_turno.cartas) == 1:
                            print("Fuiste asesinado")
                            print("Has perdido tu ultimo")
                            print("Has sido eliminado del juego")
                            jugadores.pop(asesinato)
                        else:
                            carta_perdida=int(input("fuiste asesinado "+jugadores[asesinato]+" elije que carta perder 1/2"))-1
                            jugadores[asesinato].nombre.cartas.pop(carta_perdida)
                
                #El jugador toma la accion de Intercambiar
                elif accion == "X":
                    while len(jugador_turno.cartas) != 0:
                        mazo_barajado.insert(0, jugador_turno.cartas[0])
                        jugador_turno.cartas.pop(0)
                    opciones = []
                    i = 1
                    while i <= 4:
                        num_cartas = len(mazo_barajado)
                        opciones.append(mazo_barajado[num_cartas - 1])
                        mazo_barajado.pop(num_cartas - 1)
                        i += 1
                    i = 1
                    for carta in opciones:
                        print(str(i) + "." + carta.tipo)
                        i += 1 
                    num = int(input("Escriba el numero de la primera carta que quiera elegir"))
                    carta_elegida = opciones[num - 1]
                    opciones.pop(num - 1)
                    jugador_turno.cartas.append(carta_elegida)
                    print("")
                    for carta in opciones:
                        print(str(i) + "." + carta.tipo)
                        i += 1 
                    num = int(input("Escriba el numero de la segunda carta que quiera elegir"))
                    carta_elegida = opciones[num]
                    jugador_turno.cartas.append(carta_elegida)
                    for carta in opciones:
                        mazo_barajado.append(carta)
                
                #El jugador toma la accion de Robar
                elif accion == "S":
                    r = input("¿Alguien quiere usar una Neutralizacion en contra de "  + jugador_turno.nombre + "? [S/N]").capitalize()
                    if r == "S":
                        jugador_acusa = Neutralizacion("S")
                        r = input("¿Alguien duda de esta accion?")
                    else:
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
                
                
                
                #Reaccion
                #aca debe ir un if accion =! "I" or accion =! "E" or accion =! "C":
                
                
                if accion == "T" or accion == "A" or accion == "S":
                    oposicion=input("¿alguien se opone? [S/N] ").capitalize()
                    if oposicion == "S":
                        #Jugador que se opone
                        j=1
                        print("que jugador es :")
                        for i in jugadores:
                            print("para jugador: " + i.nombre + " escriba " + str(j))
                            j+=1
                        
                        jugador_duda=int(input())
                        
                        j = 0
                        while j < len(jugadores):
                            if j == jugador_duda - 1:
                                jugador_acusa = jugadores[j]
                            j += 1
                        
                        #Llamo a la funcion
                        Duda(accion, jugador_turno, jugador_acusa)
                    
                    
                
                
                
                
                
                #Neutralizacion (counteraction)
                #Solo las acciones E (Ayuda Externa), A (Asesinato), S (Robo) pueden ser neutralizadas
                if accion == "E" or accion == "A" or accion == "S":
                    r = input("¿Alguien quiere usar una Neutralizacion en contra de "  + jugador_turno.nombre + "? [S/N]").capitalize()
                    if r == "S":
                        #Jugador que se opone
                        j=1
                        print("que jugador es :")
                        for i in jugadores:
                            print("para jugador: " + i.nombre + " escriba " + str(j))
                            j+=1
                        jugador_duda=int(input())
                        j = 0
                        while j < len(jugadores):
                            if j == jugador_duda - 1:
                                jugador_acusa = jugadores[j]
                            j += 1
                        #jugador_acusa es el jugador que usa una Neutralizacion
                        
                
                        
                
                
                #Revisar si algun jugador se quedo sin cartas
                print("")
                for j in jugadores:
                    if len(j.cartas) == 0:
                        print(j.nombre + ", has sido eliminado del juego")
                        lugar = jugadores.index(j)
                        jugadores.pop(lugar)
                
                #Revisar si solo queda un jugador
                if len(jugadores) == 1:
                    break
                
                num_jugadores = len(jugadores)
                if (turno == num_jugadores):
                    turno = 0
                turno += 1



# print("")
# #Fin del juego
# print("¡Se acabo el juego!")
# print("¡El ganador del juego es " + jugadores[0].nombre + "!")


















# #Duda a Impuestos, lo que significa que debe tener la carta Duque
        # if accion=="T" :
        #     s=0
        #     j=0
        #     while j<len(jugador_turno.cartas):
        #         if jugador_turno.cartas[j].tipo=="Duque":
        #             s=1
        #         j+=1
        #     if s==1:
        #         carta_perdida=int(input(jugador_turno.nombre + """ si tiene la carta Duque
        #                   elije que carta perder 1/2"""))-1
                
        #         jugador_duda.cartas.pop(carta_perdida)
        #     else:
        #         carta_perdida=int(input(jugador_turno.nombre + """ no tiene la carta Duque
        #                   elije que carta perder 1/2"""))-1
        #         jugador_turno.cartas.pop(carta_perdida)
                
        # #Duda al Asesinato, lo que significa que debe tener la carta Asesino        
        # elif accion=="A":
        #     s=0
        #     j=0
        #     while j<len(jugador_turno.cartas):
        #         if jugador_turno.cartas[j].tipo=="Asesino":
        #             s=1
        #         j+=1
        #     if s==1:
        #         carta_perdida=int(input(jugador_turno.nombre + """si tiene la carta Asesino
        #                   elije que carta perder 1/2"""))-1
        #         jugador_duda.cartas.pop(carta_perdida)
                
        #     else:
        #         carta_perdida=int(input(jugador_turno.nombre + """ no tiene la carta asesino
        #                   elije que carta perder 1/2"""))-1
        #         jugador_turno.cartas.pop(carta_perdida)
        
        # #Duda al Intercambio, lo que significa que debe tener la carta Embajador
        # elif accion=="X":
        #     s=0
        #     j=0
        #     while j<len(jugador_turno.cartas):
        #         if jugador_turno.cartas[j]=="Embajador":
        #             s=1
        #         j+=1
        #     if s==1:
        #         carta_perdida=int(input(jugador_turno.nombre + """ si tiene la carta Embajador
        #                   elije que carta perder 1/2"""))-1
                
        #         jugador_duda.cartas.pop(carta_perdida)
            
        #     else:
        #         carta_perdida=int(input(jugador_turno.nombre + """ no tiene la carta Embajador
        #                   elije que carta perder 1/2"""))-1
        #         jugador_turno.cartas.pop(carta_perdida)
        
        # #Duda al Robo, lo que significa que debe tener la carta Capitan
        # elif accion=="S":
        #     s=0
        #     j=0
        #     while j<len(jugador_turno.cartas):
        #         if jugador_turno.cartas[j].tipo=="Capitan":
        #             s=1
        #         j+=1    
        #     if s==1:
        #         carta_perdida=int(input(jugador_turno.nombre + """ si tiene la carta Capitan
        #                   elije que carta perder 1/2"""))-1
                
        #         jugador_duda.cartas.pop(carta_perdida)
            
        #     else:
        #         carta_perdida=int(input(jugador_turno.nombre + """ no tiene la carta Capitan
        #                   elije que carta perder 1/2"""))-1
        #         jugador_turno.cartas.pop(carta_perdida)


