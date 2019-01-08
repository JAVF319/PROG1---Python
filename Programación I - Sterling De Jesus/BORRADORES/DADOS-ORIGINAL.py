import random
import time

min = 1
max = 6
jugar = "si"

input('PROGRAMA 5\nJuego de Dados\n\nPresione enter para Lanzar')

while jugar == "si" or jugar == "s":
    print("Tirando los dados...")
    time.sleep(2)
    a=random.randint(min, max)
    b=random.randint(min, max)
    if a+b==7 or a+b==11:
        print('Tiraste {} Ganaste!!\n\n'.format(a+b))

    if a+b==2 or a+b==3 or a+b==12:
        print('Tiraste {} Perdiste!!\n\n'.format(a+b))

    if 4<=a+b<=6 or 8<=a+b<=10:
        input('Tiraste {}. Marca!  sigue tirando!\n'.format(a+b))
        continuar=True
        marca=a+b
        while continuar:
            a=random.randint(min, max)
            b=random.randint(min, max)
            if a+b==7:
                print('Tiraste {} Usted pierde :X\n'.format(a+b))
                break
            elif a+b==marca:
                print('Tiraste el {} de nuevo! Ganaste!!!!XD\n'.format(a+b))
                break
            else:
                input('Tiraste un {} sigue tirando'.format(a+b))
    continuar=False            
    jugar = input("Jugar de nuevo, s para si?")