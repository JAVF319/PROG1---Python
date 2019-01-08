"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "MAYOR, MENOR Y PROMEDIO DE LAS NOTAS (USANDO UN DICCIONARIO)".
"""

NOMBRE_MAX = None
NOTA_MAX = None
NOMBRE_MIN = None
NOTA_MIN = None
NOTA_MEAN = None
MAX = 0
MID = 0
MIN = 0

CALIFICACIONES = {'Jhon' : 100 , 'Jesus' : 80 , 'Vidal' : 99}

# ----------------- NOTA MAYOR -----------------------
for NOMBRE , NOTAS in CALIFICACIONES.items():
    if NOTA_MAX == None or NOTAS > NOTA_MAX:
        NOMBRE_MAX = NOMBRE
        NOTA_MAX = NOTAS
print ()
print ("La mayor nota es: \n", NOMBRE_MAX,NOTA_MAX)
print ()

# ----------------- NOTA MENOR -----------------------
for NOMBRE , NOTAS in CALIFICACIONES.items():
    if NOTA_MIN == None or NOTAS < NOTA_MIN:
        NOMBRE_MIN = NOMBRE
        NOTA_MIN = NOTAS
print ("La menor nota es: \n", NOMBRE_MIN,NOTA_MIN)
print ()

# ----------------- NOTA PROMEDIO --------------------
NOTA_MEAN = (NOTA_MAX+NOTA_MIN+CALIFICACIONES['Vidal'])/3
print ("La nota promedio es: \n", NOTA_MEAN)
print ()
print ("FIN")
input()