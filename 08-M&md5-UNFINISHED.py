"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "MAYOR & MENOR DE 5 NÚMEROS".
"""

NUM1 = float( input ('Introduzca el 1er. No. '))
NUM2 = float( input ('Introduzca el 2do. No. '))
NUM3 = float( input ('Introduzca el 3ro. No. '))
NUM4 = float( input ('Introduzca el 4to. No. '))
NUM5 = float( input ('Introduzca el 5to. No. '))
# Define la variable N# como un entero y espera la entrada del número.
if NUM1 > NUM2 and NUM1 > NUM3 and NUM1 > NUM4 and NUM1 > NUM5: 
    print (NUM1 ,' es el mayor. ')
elif NUM2 > NUM1 and NUM2 > NUM3 and NUM2 > NUM4 and NUM2 > NUM5:
    print (NUM2 ,' es el mayor. ')
elif NUM3 > NUM2 and NUM3 > NUM1 and NUM3 > NUM4 and NUM3 > NUM5:
    print (NUM3 ,' es el mayor. ')
elif NUM4 > NUM2 and NUM4 > NUM1 and NUM4 > NUM3 and NUM4 > NUM5:
    print (NUM4 ,' es el mayor. ')
else :
    print (NUM5 ,' es el mayor. ')
##########################################################
if NUM1 < NUM2 and NUM1 < NUM3 and NUM1 < NUM4 and NUM1 < NUM5: 
    print (NUM1 ,' es el menor. ')
elif NUM2 < NUM1 and NUM2 < NUM3 and NUM2 < NUM4 and NUM2 < NUM5:
    print (NUM2 ,' es el menor. ')
elif NUM3 < NUM2 and NUM3 < NUM1 and NUM3 < NUM4 and NUM3 < NUM5:
    print (NUM3 ,' es el menor. ')
elif NUM4 < NUM2 and NUM4 < NUM1 and NUM4 < NUM3 and NUM4 < NUM5:
    print (NUM4 ,' es el menor. ')
else :
    print (NUM5 ,' es el menor. ')
print ()
print ("FIN")
input()
