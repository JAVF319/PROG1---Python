"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ORIENTACIÓN A OBJETOS y CLASES prueba de la CLASE y el OBJETO".
"""

# En este programa se invocan funciones creadas en el OaOyC.py 
# Estan pasan a llamarse metodos del objeto "Carro" y simulan la conducción de un vehículo.
import OaOyC
Carro = OaOyC.Coche(3)
Carro.arrancar() 
Carro.conducir2()
Carro.arrancar()