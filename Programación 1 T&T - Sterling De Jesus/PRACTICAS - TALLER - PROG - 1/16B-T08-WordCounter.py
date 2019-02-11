"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "CONTADOR DE PALABRAS DE UN ARCHIVO .TXT con Excepciones". 
"""
print()
FileName = input ("Introduzca el nombre del archivo: \n")
# --------------- EXCEPCION para el error FileNotFoundError. ------------------
try:
    FileObj = open(FileName, 'r')
except FileNotFoundError as e:
    print()
    print("El archivo no existe.")
    exit()
# -----------------------------------------------------------------------------
AllWords = {}
for LINE in FileObj:
    words = LINE.split()
    for word in words:
        if word not in AllWords:
            AllWords[word] = 1
        else:
            AllWords[word] = AllWords[word] + 1
print()
print (AllWords)
# ------------ Deducción de la palabra que más se repite. -------------
Word_MAX = None
Cant_MAX = None

for W , Q in AllWords.items():
    if Cant_MAX == None or Q > Cant_MAX:
        Word_MAX = W
        Cant_MAX = Q
print ()
print ("La palabra que más se repite es: \n", Word_MAX , Cant_MAX)
print ()
print ("FIN")
input()
