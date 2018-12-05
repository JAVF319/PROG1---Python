"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ORIENTACIÓN A OBJETOS y CLASES archivo de creación de la CLASE".
"""

class Coche:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos ", gasolina, "litros.")
    
    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")
    
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan ", self.gasolina, "litros.")
        else:
            print("No se mueve.")
    def conducir2(self):
        while self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan ", self.gasolina, "litros.")
        else:
            print("No se mueve.")
            