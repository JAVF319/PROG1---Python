"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ASIGNACIÓN 1 - JUEGO DE DADOS."
"""
"""     1. Si la suma es 7 o 11 en la primera tirada, el jugador gana (se debe mostrar en pantalla: "Jugador gana!"). 
        2. Si la suma es 2, 3 o 12, en la primera tirada, ej jugador pierde. 
        3. Si la suma es 4, 5, 6, 8, 9, o 10 en la primera tirada, esa suma se convierte en la marca del jugador. 
        4. Para ganar, el jugador debe continuar lanzando los dados hasta que obtenga su marca. 
        5. El jugador pierde el juego si le sale un 7 antes de conseguir su marca.
"""

print()
print("---------   JUEGO DE DADOS   ---------\n")

import time
import random
MIN = 1
MAX = 6
LetsPlay = "yes"

input("Pulse cualquier tecla para empezar")

while LetsPlay == "yes" or LetsPlay == "y":
    time.sleep(1)
    print("Que empiece el juego, buena suerte!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".\n")

    Dado1 = random.randint(MIN, MAX)
    Dado2 = random.randint(MIN, MAX)
    
    if (Dado1 + Dado2) == 7 or (Dado1 + Dado2) == 11:
        print("Jugador gana!! Lanzaste un:", (Dado1 + Dado2))
    if (Dado1 + Dado2) == 2 or (Dado1 + Dado2) == 3 or (Dado1 + Dado2) == 12:
        print("Jugador pierde!! Lanzaste un:", (Dado1 + Dado2))
    if 4 <= (Dado1 + Dado2) <= 6 or 8 <= (Dado1 + Dado2) <= 10:
        print("-------------   Esta es tu marca!!   -------------")
        print("---------------------- ", (Dado1+Dado2), " -----------------------") 
        print("Para poder ganar, debes volver a lanzar tu marca.")
        print("OJO: Si lanzas 7 pierdes. Buena suerte!!")
        input()
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".\n")
        time.sleep(1)
        MARCA = Dado1 + Dado2
        OA = True
        while OA:
            Dado1 = random.randint(MIN, MAX)
            Dado2 = random.randint(MIN, MAX)
            if (Dado1 + Dado2) == 7:
                print("Lanzaste un", (Dado1 + Dado2), "y PERDISTE.\n")
                break
            elif (Dado1 + Dado2) == MARCA:
                print("Lanzaste un", MARCA, "otra vez y GANASTE.\n")
                break
            else:
                print("Sigue intentado, lanzaste un:", (Dado1 + Dado2))
                input()
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".\n")
                time.sleep(1)
    continuar = False            
    LetsPlay = input("Quieres seguir jugando? pulsa la letra: y.\n\n")
