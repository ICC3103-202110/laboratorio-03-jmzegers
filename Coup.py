import time
import random

#Funcion para barajar el mazo
def Barajar (mazo):
    mazo_listo = []
    i = len(mazo) - 1
    while i >= 0:
        lugar_azar = random.randint(0, i)
        carta_azar = mazo[lugar_azar]
        mazo_listo.append(carta_azar)
        mazo.pop(lugar_azar)
        i -= 1
    return mazo_listo

#Funcion para desafiar la accion de un jugador
def Duda (accion, jugador_turno, jugadores, mazo):
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
            jugador_duda2 = jugadores[j]
        j += 1
    
    s=False
    j=0
    nombre_carta = "a"
    carta_perdida = 1
    #Impuestos: tres monedas
    if accion == "T":
        nombre_carta = "Duque"
    #Asesinato
    elif accion == "A":
        nombre_carta = "Asesino"
    #Robo
    elif accion == "S":
        nombre_carta = "Capitan"
    elif accion == "X":
        nombre_carta = "Embajador"
    
    while j<len(jugador_turno.cartas):
        if jugador_turno.cartas[j].tipo == nombre_carta:
            s=True
            carta_a_botar = jugador_turno.cartas[j]
            ind_carta_a_botar = j
            break
        j+=1
    
    #El jugador sí tiene la carta
    if s==True:
        carta_perdida=int(input(jugador_turno.nombre + " si tiene la carta "  + nombre_carta + "elije que carta perder 1/2"))-1
        jugador_duda2.cartas.pop(carta_perdida)
        
        #El jugador pierde la carta y la agrega al mazo
        print(jugador_turno.nombre + " tiene que botar la carta que ha revelado y ponerla en el mazo")
        mazo.insert(0, carta_a_botar)
        jugador_turno.cartas.pop(ind_carta_a_botar)
        
        #El mazo se baraja
        print("Luego, se baraja nuevamente el mazo")
        mazo_barajado = Barajar(mazo)
        tamanno_mazo = len(mazo_barajado) - 1
        
        #El jugador saca la ultima carta del mazo
        print("Por ultimo, se le agrega una carta nueva a la mano")
        jugador_turno.cartas.append(mazo_barajado(tamanno_mazo))
        
    else:
        carta_perdida=int(input(jugador_turno.nombre + " no tiene la carta " + nombre_carta + " elije que carta perder 1/2"))-1
        jugador_turno.cartas.pop(carta_perdida)

    return s

#Funcion para neutralizar la accion del jugador    
def Neutralizacion (accion, jugador_turno, jugadores):
    j=1
    print("que jugador es :")
    for i in jugadores:
        if i != jugador_turno:
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
def Duda_Neutralizacion (accion, jugador_acusado, jugadores, mazo):
    j=1
    print("Elija que jugador es :")
    for i in jugadores:
        if i != jugador_acusado:
            print("para jugador: " + i.nombre + " escriba " + str(j))
        j+=1
    jugador_duda=int(input())
    j = 0
    while j < len(jugadores):
        if j == jugador_duda - 1:
            jugador_acusa = jugadores[j]
        j += 1
    tiene_carta = False
    nombre_carta2 = "a"
    if accion == "E":
        nombre_carta = "Duque"
    elif accion == "A":
        nombre_carta = "Condesa"
    elif accion == "S":
        nombre_carta = "Embajador"
        nombre_carta2 = "Capitan"
    for c in jugador_acusado.cartas:
        if c.tipo == nombre_carta or c.tipo == nombre_carta2:
            tiene_carta = True
            carta_a_botar = jugador_acusado.cartas[j]
            ind_carta_a_botar = j
            break
    if tiene_carta == True:
        print(jugador_acusado + " tiene la carta adecuada!")
        
        carta_perdida=int(input(jugador_acusado.nombre + " si tiene la carta "  + nombre_carta + "elije que carta perder 1/2"))-1
        jugador_acusa.cartas.pop(carta_perdida)
        
        #El jugador pierde la carta y la agrega al mazo
        print(jugador_acusado.nombre + " tiene que botar la carta que ha revelado y ponerla en el mazo")
        mazo.insert(0, carta_a_botar)
        jugador_acusado.cartas.pop(ind_carta_a_botar)
        
        #El mazo se baraja
        print("Luego, se baraja nuevamente el mazo")
        mazo_barajado = Barajar(mazo)
        tamanno_mazo = len(mazo_barajado) - 1
        
        #El jugador saca la ultima carta del mazo
        print("Por ultimo, se le agrega una carta nueva a la mano")
        jugador_acusado.cartas.append(mazo_barajado(tamanno_mazo))
        
    else:
        carta_perdida=int(input(jugador_acusado.nombre + " no tiene la carta " + nombre_carta + " elije que carta perder 1/2"))-1
        jugador_acusado.cartas.pop(carta_perdida)
        
    return tiene_carta

def Asesinar (jugadores, jugador_turno):
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
        
def Intercambio (jugador_turno, mazo_barajado):
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
        
def Robo (jugadores, jugador_turno):
    j = 0
    a = True
    while a == True:
        print("Elija al jugador al que quiera robar: ")
        for i in jugadores:
            if i != jugador_turno:
                print("para jugador: " + i.nombre + " escriba " + str(j))
            j+=1
        num_jugador=int(input())
        j = 0
        while j < len(jugadores):
            if j == num_jugador:
                jugador_a_robar = jugadores[j]
            j += 1
        if jugador_a_robar.num_monedas == 0:
            print("Este jugador no tiene suficientes monedas")
        else:
            if jugador_a_robar.num_monedas == 1:
                print("Este jugador solo tiene una moneda")
                jugador_a_robar.num_monedas -= 1
                jugador_turno.num_monedas += 1
            else:
                jugador_a_robar.num_monedas -= 2
                jugador_turno.num_monedas += 2
            break



class Coup:
    def Juego(jugadores, mazo_barajado):
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
                    
                    elif accion == "S":
                        for j in jugadores:
                            if j != jugador_turno:
                                if j.num_monedas > 0:
                                    puede_realizar = "s"
                        if puede_realizar == "n":
                            print("Ninguno de los jugadores tiene suficientes monedas")
                        
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
                
                #El jugador toma la accion de Cobrar Impuestos
                elif accion == "T":
                    oposicion=input("¿Alguien quiere desafiar esta accion? [S/N] ").capitalize()
                    if oposicion == "S":
                        #Llamo a la funcion
                        tiene_carta = Duda(accion, jugador_turno, jugadores, mazo_barajado)
                        
                        #Se lleva a cabo la accion normalmente
                        if tiene_carta == True:
                            jugador_turno.num_monedas += 3
                        
                    else:
                        jugador_turno.num_monedas += 3
                
                    
                
                #El jugador toma la accion de Hacer un Golpe
                elif accion == "C":
                    print("a quien desea hacer el golpe?")
                    j=0
                    for i in jugadores:
                        if i.nombre!=jugador_turno.nombre:
                            print("para jugador: " + i.nombre + " escriba " + str(j))
                        j+=1
                    golpe=int(input())
                    j = 0
                    while j < len(jugadores):
                        if j == golpe - 1:
                            jugador_golpeado = jugadores[j]
                        j += 1
                    
                    if len(jugador_golpeado.cartas)==1:
                        jugador_golpeado.cartas.pop(0)
                    else:
                        carta_perdida=int(input("te hicieron un golpe "+jugador_golpeado.nombre+" elije que carta perder 1/2"))-1
                        jugador_golpeado.cartas.pop(carta_perdida)
                
               
                
               
                
               #El jugador toma la accion de Ayuda Externa
                #Esta accion puede ser bloqueada
                #por un jugador que tenga la carta de Duque
                elif accion == "E":
                    neutr = input("¿Alguien quiere neutralizar la accion del jugador? [S/N]").capitalize()
                    if neutr == "S":
                        jugador_acusa = Neutralizacion(accion, jugador_turno, jugadores)
                        
                        duda_neutr = input("¿Alguien desafia esta Neutralizacion? [S/N]").capitalize()
                        if duda_neutr == "S":
                            tiene_carta = Duda_Neutralizacion(accion, jugador_acusa, jugadores, mazo_barajado)
                    else:
                        jugador_turno.num_monedas += 2
                
                #El jugador toma la accion de Asesinar
                elif accion == "A":
                    jugador_turno.num_monedas -= 3
                    
                    oposicion=input("¿Alguien quiere desafiar esta accion? [S/N] ").capitalize()
                    if oposicion == "S":

                        #Llamo a la funcion
                        tiene_carta = Duda(accion, jugador_turno, jugadores, mazo_barajado)
                        
                        #Se lleva a cabo la accion normalmente
                        if tiene_carta == True:
                                Asesinar(jugadores, jugador_turno)
                    else:
                        neutr = input("¿Alguien quiere neutralizar la accion del jugador? [S/N]").capitalize()
                        if neutr == "S":
                            jugador_acusa = Neutralizacion(accion, jugador_turno, jugadores)
                            
                            duda_neutr = input("¿Alguien desafia esta Neutralizacion? [S/N]").capitalize()
                            if duda_neutr == "S":
                                tiene_carta = Duda_Neutralizacion(accion, jugador_acusa, jugadores, mazo_barajado)
                            
                        else:
                            Asesinar(jugadores, jugador_turno)

                
                #El jugador toma la accion de Intercambiar
                elif accion == "X":
                    oposicion=input("¿Alguien quiere desafiar esta accion? [S/N] ").capitalize()
                    if oposicion == "S":
                        #Llamo a la funcion
                        tiene_carta = Duda(accion, jugador_turno, jugadores, mazo_barajado)
                        #Se lleva a cabo la accion normalmente
                        if tiene_carta == True:
                            Intercambio(jugador_turno, mazo_barajado)
                    
                    else:
                        Intercambio(jugador_turno, mazo_barajado)
                    
                
                #El jugador toma la accion de Robar
                elif accion == "S":
                    oposicion=input("¿Alguien quiere desafiar esta accion? [S/N] ").capitalize()
                    if oposicion == "S":
                        #Llamo a la funcion
                        tiene_carta = Duda(accion, jugador_turno, jugadores, mazo_barajado)
                        #Se lleva a cabo la accion normalmente
                        if tiene_carta == True:
                            Robo(jugadores, jugador_turno)
                    else:
                        neutr = input("¿Alguien quiere neutralizar la accion del jugador? [S/N]").capitalize()
                        if neutr == "S":
                            jugador_acusa = Neutralizacion(accion, jugador_turno, jugadores)
                            
                            duda_neutr = input("¿Alguien desafia esta Neutralizacion? [S/N]").capitalize()
                            if duda_neutr == "S":
                                tiene_carta = Duda_Neutralizacion(accion, jugador_acusa, jugadores, mazo_barajado)
                            
                        else:
                            Robo(jugadores, jugador_turno)
                        
                
                
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
                i=0
                while i<num_jugadores:
                    jugadores[i].numero=i+1
                    i+=1
                if turno >= num_jugadores:
                    
                    turno = 0
                turno += 1
                
            
          print("")
          #Fin del juego
          print("¡Se acabo el juego!")
          print("¡El ganador del juego es " + jugadores[0].nombre + "!")