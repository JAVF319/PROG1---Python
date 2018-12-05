"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ASIGNACIÓN 2 - CONTADOR DE VOCALES."
"""
"""     1. Debe abrir un archivo en formato txt. 
        2. Mostrar en pantalla la cantidad de vocales existentes en el archivo.
        3. El programa debe mostrar la cantidad de vocales de forma independiente. 
"""
# ------------------------------------------------------
# Contenido del archivo "Vocales.txt".
"""     aaaaaeeeeiiioou 
        eeeeiiioouaaaaa
        iiioouaaaaaeeee
        oouaaaaaeeeeiii
        uaaaaaeeeeiiioo
"""

print()
print("---------   CONTADOR DE VOCALES   ---------\n")

VOCALES = []
CantA = []
CantE = []
CantI = []
CantO = []
CantU = []
FileName = input ("Introduzca el nombre del archivo: \n")

try:
    FileObj = open(FileName, 'r')
except FileNotFoundError as e:
    print()
    print("El archivo no existe.")
    exit()

for Linea in FileObj:
    Palabra = Linea.split()
    for Letra in Palabra:
        VOCALES.append(Letra)

print()
print("Este es el contenido del archivo Vocales.txt: \n")
print(VOCALES)
print()

for Vocal in VOCALES:
    a = Vocal.count("a")
    á = Vocal.count("á")
    CantA.append(a)
    CantA.append(á)
        
    e = Vocal.count("e")
    é = Vocal.count("é")
    CantE.append(e)
    CantE.append(é)
    
    i = Vocal.count("i")
    í = Vocal.count("í")
    CantI.append(i)
    CantI.append(í)
        
    o = Vocal.count("o")
    ó = Vocal.count("ó")
    CantO.append(o)
    CantO.append(ó)
    
    u = Vocal.count("u")
    ú = Vocal.count("ú")
    ü = Vocal.count("ü")
    CantU.append(u)
    CantU.append(ú)
    CantU.append(ü)
    
print("A: ", sum(CantA))
print("E: ", sum(CantE))
print("I: ", sum(CantI))
print("O: ", sum(CantO))
print("U: ", sum(CantU))
print()
input()