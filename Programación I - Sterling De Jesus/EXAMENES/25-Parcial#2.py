"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "PARCIAL #2 - Analisis de Generación Semanal."
"""
"""
1. Abrir un archivo llamado: "historico_generacion.txt".
2. Generar un archivo llamado: "resumen.txt" con lo siguiente
    i. Promedio de generacion de cada semana.
    ii. La semana de mayor generacion, y el dia de mayor generacion de dicha semana. 
    iii. La semana de menor generacion, y el dia de menor generacion de dicha semana.
"""

print()
print("---------   ARCHIVO DE ANALISIS DE GENERACIÓN   ---------\n\n")

import math
ProGENpSemana=[]
GENpDia=[]
C=0    

try:
    with open("historico_generacion.txt", "rt") as HistoricoGeneracion:
        for L in HistoricoGeneracion:
            if L.find('@') >= 0:
                PosInicial = L.find('@')
                PosFinal = L.find('MW')
                DIAmasGEN= L[PosInicial:PosFinal]
                for GENenMW in DIAmasGEN.split(): 
                    if GENenMW.isdigit():
                        GENpDia.append(int(GENenMW))

    while C < int(len(GENpDia)):
        ProGENpSemana.append(sum(GENpDia[C:C+7]))
        C+=7

    Resumentxt=open('resumen.txt', mode='w')
    Resumentxt.write('                   ANALISIS DEL REG. DE GENERACIÓN                  '+'\n\n')
    i=1
    Resumentxt.write("----------------- Promedios de Generación por Semana ---------------\n\n")
    for PRO in ProGENpSemana:
        Resumentxt.write("Generación de la semana #{} es: {} MW.\n".format(i,PRO))
        i+=1
    SemanadMAXGen=ProGENpSemana.index(max(ProGENpSemana))+1
    SemanadMINGen=ProGENpSemana.index(min(ProGENpSemana))+1
    MAXD=GENpDia.index(max(GENpDia))+1
    D=['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
    Resumentxt.write("\n----------------- MAX/MIN de Generación por Semana ---------------")
    Resumentxt.write('\n\nLa máxima generación por semana fue la #{} con: {} MW.'.format(SemanadMAXGen,max(ProGENpSemana)))
    Resumentxt.write('\nLa menor generación por semana fue la #{} con: {} MW.\n'.format(SemanadMINGen,min(ProGENpSemana)))
    Resumentxt.write("\n----------------- Día de MAX Generación y su Semana ---------------")
    Resumentxt.write('\n\nDía: {}. Semana #{} con: {} MW.\n'.format(D[int((MAXD-1)%7)], int(math.ceil(MAXD/7)), max(GENpDia)))
    Resumentxt.close()

    print('Un nuevo archivo: "resumen.txt" ha sido generado.\n')

except FileNotFoundError as e:
    print('El archivo "historico_generacion.txt" no existe.\n')
                    

