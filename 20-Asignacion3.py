"""     PROGRAMADOR:    José A. Vidal F.
        MATRICULA:      2-15-6573.
        PROGRAMA:       "ASIGNACIÓN 3 - Reemplazador de Palabras."
"""
"""     Escribir una función de nombre replace(text_string, replace_string) que tome 
        dos strings como entrada, y retorne un nuevo string donde la primera ocurrencia 
        de replace_string sea sustituida por la palabra "bandulo".

        Ejemplo:    replace("Como estas mi buen amigo?", "amigo"), 
                    debe retornar el string: "Como estas mi buen bandulo?"
        
        Notas:  1. string_1.find(string_2) returna la posicion de la primera ocurrencia 
                  de string_2 en string_1.
                2. len(string) retorna la longitud de string.
                3. No usar la función input dentro de la función replace.
                4. Adjuntar solamente el código fuente de la función (extensión .py). 
"""

BANDULO = str("Bandulo")
text_string = input("\nIntroduzca el primer String donde desea reemplazar: \n")
replace_string = input("\nIntroduzca el String que desea sustituir por la palabra 'BANDULO': \n")

def replace(old, new):
    print("El nuevo String a presentar es: \n")
    print(text_string.replace(replace_string, BANDULO, 1))

replace(replace_string, BANDULO)
input()