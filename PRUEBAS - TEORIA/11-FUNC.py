"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "PROBANDO FUNCIONES - I".
"""

# Cantidad de parametros fija.
input()  
def FUNC (p1, p2, p3):
    print ("Cantidad de parametros fija.")
    print (p1)
    print (p2)
    print (p3*p2)
    print ("----------------")
FUNC (1, 2, 3)

# Valores por defecto para parametros. 
input ()
print("Valores por defecto para parametros.")
def FUNC2 (p00, p0 = 'PRUEBA'):
    print ("Esta es la prueba de una FUNCIÓN en Python con valores por defecto:\n", p0*p00)
    print ("----------------")
FUNC2 (3)

# No. variable de argumentos en una función.
input ()
print("No. variable de argumentos.")
def FUNC3 (p4, *otros):
    for val in otros:
        print (val)
FUNC3 (3, 6, 9)
print ("----------------")
print ()
print ("FIN")
input()
