"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "PARCIAL #1 - Calculadora del precio de kWh."
"""
""" --------- CONDICIONES --------- 
A) <= 350 kWh, = RD$ 6.15
B) <= 560 kWh, = RD$ 7.34 
C) <= 1300 kWh, el calculo a realizar sera: 
     i. Los primeros 200 kWh serán calculados a RD$ 4.35
     ii. Los siguientes 360 kWh serán calculados a un precio de RD$ 6.50
     iii. Los restantes kWh deben ser calculados a un precio de RD$ 9.69
D) > 1300 kWh tendrá las siguientes condiciones: 
     i. Los primeros 600 kWh tendrán un costo de RD$ 8.25
     ii. Los restantes kWh deben ser calculados a un valor de RD$ 11.65
E) > 300 kWh deberán pagar un cargo fijo de RD$ 350.
"""

print()
print("---------   CALCULADORA DE KILOWATTS/RD$   ---------\n\n")

kWh = float(input("Introduzca los kiloWatts consumidos: "))
Td350 = 6.15
Td560 = 7.34
Td200 = 4.35 * 200
Td360 = 6.50 * 360
Td1300 = (kWh-200-360) * 9.69
Td600 = 8.25 * 600
Td1301 = (kWh-600) * 11.65
TaP = 0

if kWh < 350:
    TaP = (kWh * Td350)
    if kWh > 300: 
         print("\nEl total a pagar es de: ", TaP+350)
    else:
          print("\nEl total a pagar es de: ", TaP)

elif 350 <= kWh < 560:
     TaP = (kWh * Td560)+350
     print("\nEl total a pagar es de: ", TaP+350)

elif 560 <= kWh < 1300:
     TaP = (Td1300+Td200+Td360+350)
     print("\nEl total a pagar es de: ", TaP)

else:
     Tap = (Td600+Td1301+350)
     print("\nEl total a pagar es de: ", Tap)
input()