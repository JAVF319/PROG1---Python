"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "MAYOR & MENOR DE DOS NÚMEROS".
"""

NUM1 = float( input ('Introduzca un No. '))
# Define la variable NUM1 como un entero y espera la entrada del número.
NUM2 = float( input ('Introduzca otro No. '))
# Define la variable NUM2 como un entero y espera la entrada del número.
if NUM1 > NUM2 : 
    print (NUM1 , 'es mayor que' , NUM2)
# Define la primera condición para hacer la comparación y muestra un msj. 
# si se cumple dicha condición.
elif NUM2 > NUM1 :
    print (NUM2 , 'es mayor que' , NUM1)
# Establece la segunda condición (de forma implicita) y muestra un msj. 
# si no se cumple la primera condición.
else :
    print ('Ambos números son iguales')
print ()
print ("FIN")
input()