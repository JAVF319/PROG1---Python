"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "COMPRENSIÓN DE LISTAS".
"""

# Con este proceso podemos agregar elementos a una lista automaticamente. 
L2 = []
T2 = []
L = [1,2,3,4,5]
T = (6, 7, 8, 9, 10)
print (L , "Valores en L.")
print (T , "Valores en T.")
input()

# Método tradicional utilizando FUNC.
print ("---------- VALORES x 2 ----------")
for valoresL in L:
    L2.append(valoresL*2)
print(L2 , "Valores en L x 2.")
for valoresT in T:
    T2.append(valoresT*2)
print(T2 , "Valores en T x 2.\n")
input()

# Método empleando COMPRENSIÓN DE LISTAS.
print ("---------- VALORES x 3 ----------")
R3 = [valoresL*3 for valoresL in L]
print (R3 , "Valores en L x 3.")
T3 = [valoresT*3 for valoresT in T]
print (T3 , "Valores en T x 3.\n") 
input()

# PROG. "Números pares e impares en L."
ImparL = [valoresL for valoresL in L if valoresL%2 != 0]
print(ImparL , "Valores IMPARES en L.")
ParL = [valoresL for valoresL in L if valoresL%2 == 0]
print(ParL , "Valores PARES en L.")
input()

# PROG. "Números pares e impares en T."
ImparT = [valoresT for valoresT in T if valoresT%2 != 0]
print(ImparT , "Valores IMPARES en T.")
ParT = [valoresT for valoresT in T if valoresT%2 == 0]
print(ParT , "Valores PARES en T.")
print ()
print ("FIN")
input()