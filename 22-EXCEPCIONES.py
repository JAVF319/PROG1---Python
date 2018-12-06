"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "Prueba de EXCEPCIONES". 
"""

n = float(input("Número 1: "))
p = float(input("Número 2: "))

try:
    resultado = n/p
except: 
    print("No se puede dividir por cero.")
    exit()
print("El resultado es: ", resultado)
input()

# ------------------------------------------
try:
    pass
except expression as identifier:
    pass
else:
    pass
finally:
    pass
# ---------------------------------------
"""     except:
Es una forma general de captar una excepción.
        except ZeroDivisionError as E001:  
Es una forma más específica de captar una excepción
detallando la excepcion que quiero captar y convirtiendola en una variable llamada E001.
"""
