print("Calculadora de consumo kwh/RD$")
consumo = float(input("Introducir consumo en kwh: \n"))

if consumo <= 350:
    consumo *= 6.15
elif consumo > 350 and consumo <= 560:
    consumo *= 7.34
elif consumo > 560 and consumo <= 1300:
    a = 200 * 4.35
    b = 360 * 6.5
    consumo -= 560
    consumo *= 9.69
    consumo += (a + b)
elif consumo > 1300:
    a = 600 * 8.25
    consumo -= 600
    consumo *= 11.65
    consumo += a
    
if consumo > 300:
    consumo += 350
    
consumo = round(consumo, 2) 

print(consumo)

