import random

MIN = 0
MAX = 10

NoGanador = random.randint(MIN, MAX)

TRY = 7
while (TRY != 0):
    IN = int(input("Introduzca un número por favor: "))
    if IN == NoGanador:
        print("GANASTE.")
        input()
        exit()
    else:
        print("INTENTA DE NUEVO.")
        if IN > NoGanador:
            print("Baja un poco.")
        else:
            print("Sube un poco.")
    TRY -= 1
print("El número ganador era: ",NoGanador)
input()
