"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "CONTADOR DE PALABRAS DE UN ARCHIVO .TXT". 
"""

print()
FileName = input ("Introduzca el nombre del archivo: ")
# El archivo debe encontrarse en el mismo directorio (carpeta).
FileObj = open(FileName, 'r')
# El comando "open()" permite abrir archivos 
# Se debe especificar si es en modo solo lectura (r) o escritura (w).
# Si el modo es (r) y el archivo no es encontrado ocurre un error/excepción.
# Si el modo es (w) y el archivo no es encontrado ocurre una excepción y se crea un archivo con el nombre introducido anteriormente.
AllWords = {}
# Diccionario para almacenar las palabras y la cant. de veces que se repiten.
for LINE in FileObj:
    words = LINE.split()
    for word in words:
        if word not in AllWords:
            AllWords[word] = 1
        else:
            AllWords[word] = AllWords[word] + 1
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
