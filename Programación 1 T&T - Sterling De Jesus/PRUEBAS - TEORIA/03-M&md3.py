"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "MAYOR & MENOR DE TRES NÚMEROS".
"""

NUM1 = float( input ('Introduzca el 1er. número: '))
# Define la variable NUM1 como un entero y espera la entrada del número.
NUM2 = float( input ('Introduzca el 2do. número: '))
NUM3 = float( input ('Introduzca el 3er. número: '))
if NUM1 > NUM2 and NUM1 > NUM3: 
    print (NUM1 ,' es mayor que: ', NUM2, 'y', NUM3)
# Define la primera condición para hacer la comparación y muestra un msj. 
# Si se cumple dicha condición.
elif NUM2 > NUM1 and NUM2 > NUM3:
    print (NUM2 ,' es mayor que: ', NUM1, 'y', NUM3)
# Establece la segunda condición para hacer la comparación y muestra un msj. 
# Si no se cumple la condición anterior.
elif NUM3 > NUM1 and NUM3 > NUM2:
    print (NUM3 ,' es mayor que: ', NUM1, 'y', NUM2)
# Establece la tercera condición para hacer la comparación y muestra un msj.
# si no se cumple la condición anterior.
else :
    print ('Todos los números son iguales')
# Si no se cumple ninguna de las condiciones anteriores, muestra un msj.
print ()
print ("FIN")
input()