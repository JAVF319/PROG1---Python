"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ASIGNACIÓN 4 - HORAS EXTRA." Modificado con conteo real de HE en comparación al 21A.
"""
"""     1. Determinar el monto a pagar mensual por las horas extra (HE) trabajadas.
        2. Las horas ordinarias (HO) cuestan US$ 9.60.
        3. Si exceden las 40 horas semanales, las HE deben pagarse a 1.75 veces el valor de una HO.
        4. Si se hacen 15 HE o más mensuales se paga un incentivo de US$ 450. 
"""

print()
print("---------   Calculador de Horas Extra Trabajadas   ---------\n")
TTdHES = []
TTdHEM = []
CantdeSemanas = int (4)
i = 1
while (CantdeSemanas > 0) :
    CdHES = float (input ("Introduzca la cant. total de horas trabajadas en la Semana #" + str(i) +": "))
    if CdHES <= 40:
        Semana1 = 0
        TTdHES.append(Semana1)
        TTdHEM.append(Semana1)
        # print ("No califica para pago de horas extra.")
    else: 
        Semana1 = (CdHES-40)*9.60*1.75
        TTdHES.append(Semana1)
        TTdHEM.append(CdHES-40)
        # print ("El monto a pagar es de US$: ", (CdHES-40)*9.60*1.75)
    i = i + 1
    CantdeSemanas = CantdeSemanas - 1
print()
DineroHESinIncentivos = sum(TTdHES)
HETTMensuales = sum(TTdHEM)
if HETTMensuales >= 15:
    print ("El monto a pagar por Horas Extra trabajadas es de US$: ", DineroHESinIncentivos+450)
else:
    print ("El monto a pagar por Horas Extra trabajadas es de US$: ", DineroHESinIncentivos)
input()