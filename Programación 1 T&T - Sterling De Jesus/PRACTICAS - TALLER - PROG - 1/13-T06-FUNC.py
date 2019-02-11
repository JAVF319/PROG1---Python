"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "PROBANDO FUNCIONES - II".
"""

# PROG. "Suma de dos números usando funciones".
n1 = float (input ("No. 1: "))
n2 = float (input ("No. 2: "))

def SUMA (a,b):
        return a+b
print ("La SUMA es: ", SUMA(n1,n2))
print ("La SUMA2 es: ", SUMA(n1,n2) + SUMA(n1,n2) )
print ("----------------")
input ()

# PROG. "Mayor de dos números usando funciones".
def MAYOR (a,b):
        if a>b:
                return a
        else:
                return b
NoMayor = MAYOR (n1,n2)
print ("El MAYOR es: ", NoMayor)
input ()

# PROG. "SUMATORIA de los numeros hasta el número MAYOR introducido".
N = NoMayor
def SUMATORIA (S):
        Suma = 0
        C = 0
        while (C < (N+1)) :
                Suma = Suma + C
                C = C + 1
        print ("El resultado de la sumatoria es: ", Suma)
SUMATORIA (N)
input ()

# PROG. "FACTORIAL de los numeros hasta el número MAYOR introducido".
F = N
def FACTORIAL (F):
        Factor = 1
        j = 1
        while j <= F:
                Factor = Factor + j
                j = j + 1
        print ("El resultado del factorial es: ", Factor)
FACTORIAL (F)
print ()
print ("FIN")
input()