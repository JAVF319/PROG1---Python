"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "SUMATORIA DE LOS VALORES HASTA EL NÚMERO (+) INTRODUCIDO".
"""

N = int ( input ("Introduzca un número entero positivo: "))
if N <= 0:
    print ("El número introducido no es válido")
else:
    Suma = 0
    C = 0
    while (C < (N+1)) :
        Suma = Suma + C
        C = C + 1
    print ("El resultado de la suma es: ", Suma)
print ()
print ("FIN")
input()
