"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "MAYOR & MENOR DE 5 NÚMEROS".
"""

Lista = []
# Crea una lista donde puedo guardar todos los valores a introducir. 
Cantidad = int (5)
# Crea una variable de tipo ENTERO con valor definido en 5.
# Con esta puedo definir más adelante cuantos valores podré introducir en la lista.
MAYOR = 0
menor = 0   
# Crea dos variables con valor inicial en 0 (L10,11).
# Luego puedo asignarles los valores "mayor y menor" de la lista con la función "min" y "max".
i = 1
while (Cantidad > 0) :
    Numero = float ( input ( "Introduzca el #" + str(i) + " : "))
# Crea una variable de tipo DECIMAL que espera la introducción de un número.
# "str(i)" actua como indicador del número introducido. 
    Lista.append(Numero)
# Agrega los valores introducidos a la lista.
    i = i + 1
# Sirve para simular la introducción de un nuevo número al asignar un valor #n o #n+1 a L17.
    Cantidad = Cantidad - 1
MAYOR = max(Lista)    
menor = min(Lista)
# Las variables reciben los valores MAX=Mayor y MIN=Menor de los introducidos en la lista. 
print("El mayor es: ", MAYOR)
print("El menor es: ", menor)
print ()
print ("FIN")
input()