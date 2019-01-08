# fileLines = []
# with open('./historico_generacion.txt', 'r') as _:
#     for line in _:
#         line = line.strip()
#         if line:
#             fileLines.append(line)
f = open('./historico_generacion.txt', 'r')
fileLines = f.readlines()

weeksLines = fileLines[6:-1]

# Dividir data en Semanas
dataPerWeeks = {}
lastWeek = None
for line in weeksLines :
    line = line.strip()
    if line:
        if 'SEMANA' in line :
            lastWeek = line.split(': ')[1]
            dataPerWeeks[lastWeek] = []
        elif lastWeek is not None :
            dataPerWeeks[lastWeek].append(line)

# values per day
daysGroupByWeeks = {}
daysGroupByWeeks['weeks'] = {}
daysGroupByWeeks['minWeek'] = None
daysGroupByWeeks['maxWeek'] = None
for week in dataPerWeeks.keys() :
    # daysGroupByWeeks = {}
    dicWeek = {}
    dicWeek['days'] = {}
    dicWeek['average'] = 0
    dicWeek['unit'] = ''
    dicWeek['min'] = None
    dicWeek['max'] = None

    for day in dataPerWeeks[week] :
        values = day.split('@')
        dayName = values[1].strip()
        value = values[-1].strip().split(' ')
        dicWeek['unit'] = value[1]
        dicWeek['days'][dayName] = float(value[0])
        day = dicWeek['days'][dayName]
        dicWeek['average'] += day

        if dicWeek['min'] is None or day < dicWeek['min'] :
            dicWeek['min'] = day
            dicWeek['minName'] = dayName

        if dicWeek['max'] is None or day > dicWeek['max'] :
            dicWeek['max'] = day
            dicWeek['maxName'] = dayName

    dicWeek['average'] /= len(dicWeek['days'])
    dicWeek['average'] = round(dicWeek['average'], 2)
    daysGroupByWeeks['weeks'][week] = dicWeek

    if daysGroupByWeeks['minWeek'] is None or daysGroupByWeeks['minWeek']['min'] > dicWeek['min']:
        daysGroupByWeeks['minWeek'] = dicWeek
        daysGroupByWeeks['minWeek']['weekNumber'] = week
    if daysGroupByWeeks['maxWeek'] is None or daysGroupByWeeks['maxWeek']['max'] < dicWeek['max']:
        daysGroupByWeeks['maxWeek'] = dicWeek
        daysGroupByWeeks['maxWeek']['weekNumber'] = week

f = open('./resumen.txt', 'w+')

f.write('La semana de mayor generacion {}, y el dia de mayor generacion de dicha semana {} \n'.format(daysGroupByWeeks['maxWeek']['weekNumber'], daysGroupByWeeks['maxWeek']['maxName']))
f.write('La semana de menor generacion {}, y el dia de menor generacion de dicha semana {} \n'.format(daysGroupByWeeks['minWeek']['weekNumber'], daysGroupByWeeks['minWeek']['minName']))
f.write('Promedio de generacion de cada semana.\n \n')
for weekNumber in daysGroupByWeeks['weeks'].keys():
    week = daysGroupByWeeks['weeks'][weekNumber]
    f.write('SEMANA {} promedio {} {} \n'.format(weekNumber, week['average'], week['unit']))