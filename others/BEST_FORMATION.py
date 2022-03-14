from json import load
from others.FILL_BEST_FORMATION import *
from openpyxl import load_workbook

def sorting_criteria(item):
    return item[2]

def create_best_formation(portieri, difensori, centrocampisti, attaccanti, team_name):
    counter_role = {'P':0, 'D':0, 'C':0, 'A':0}
    best_formation = [[], [], [], []]
    total = 0

    index_dd = 0
    index_cc = 0
    index_att = 0


    player = portieri.pop(0)
    best_formation[0].append(player[0])
    counter_role['P'] += 1

    total += player[2]

    if index_att < len(attaccanti):
        attaccante = attaccanti[index_att]
        index_att += 1
    else:
        attaccante = ['Non gioca', 'A', 0]
    best_formation[3].append(attaccante[0])
    counter_role['A'] += 1

    total += player[2]

    for index in range(3):
        if index_dd < len(difensori):
            difensore = difensori[index_dd]
            index_dd += 1
        else:
            difensore = ['Non gioca', 'D', 0]
        best_formation[1].append(difensore[0])
        counter_role['D'] += 1

        total += difensore[2]

        if index_cc < len(centrocampisti):
            centrocampista = centrocampisti[index_cc]
            index_cc += 1
        else:
            centrocampista = ['Non gioca', 'C', 0]
        best_formation[2].append(centrocampista[0])
        counter_role['C'] += 1

        total += player[2]


    while (len(best_formation[0]) + len(best_formation[1]) + len(best_formation[2]) + len(best_formation[3])) < 11:
        if counter_role['D'] == 5:
            if index_cc < len(centrocampisti):
                centrocampista = centrocampisti[index_cc]
            else:
                centrocampista = ['Non gioca', 'C', 0]
            if index_att < len(attaccanti):
                attaccante = attaccanti[index_att]
            else:
                attaccante = ['Non gioca', 'A', 0]
            if centrocampista[2] <= attaccante[2]:
                best_formation[2].append(centrocampista[0])
                index_cc += 1
                counter_role['C'] += 1
                total += centrocampista[2]
            else:
                best_formation[3].append(attaccante[0])
                index_att += 1
                counter_role['A'] += 1
                total += attaccante[2]

        elif counter_role['C'] == 5:
            if index_dd < len(difensori):
                difensore = difensori[index_dd]
            else:
                difensore = ['Non gioca', 'D', 0]
            if index_att < len(attaccanti):
                attaccante = attaccanti[index_att]
            else:
                attaccante = ['Non gioca', 'A', 0]
            if difensore[2] <= attaccante[2]:
                best_formation[3].append(attaccante[0])
                index_att += 1
                counter_role['A'] += 1
                total += attaccante[2]
            else:
                best_formation[1].append(difensore[0])
                index_dd += 1
                counter_role['D'] += 1
                total += difensore[2]

        elif counter_role['A'] == 3:
            if index_dd < len(difensori):
                difensore = difensori[index_dd]
            else:
                difensore = ['Non gioca', 'D', 0]
            if index_cc < len(centrocampisti):
                centrocampista = centrocampisti[index_cc]
            else:
                centrocampista = ['Non gioca', 'C', 0]
            if difensore[2] < centrocampista[2]:
                best_formation[2].append(centrocampista[0])
                index_cc += 1
                counter_role['C'] += 1
                total += centrocampista[2]
            else:
                best_formation[1].append(difensore[0])
                index_dd += 1
                counter_role['D'] += 1
                total += difensore[2]

        else:
            if index_dd < len(difensori):
                difensore = difensori[index_dd]
            else:
                difensore = ['Non gioca', 'D', 0]
            if index_cc < len(centrocampisti):
                centrocampista = centrocampisti[index_cc]
            else:
                centrocampista = ['Non gioca', 'C', 0]
            if index_att < len(attaccanti):
                attaccante = attaccanti[index_att]
            else:
                attaccante = ['Non gioca', 'A', 0]

            if difensore[2] < centrocampista[2]:
                if centrocampista[2] < attaccante[2]:
                    best_formation[3].append(attaccante[0])
                    index_att += 1
                    counter_role['A'] += 1
                    total += attaccante[2]
                else:
                    best_formation[2].append(centrocampista[0])
                    index_cc += 1
                    counter_role['C'] += 1
                    total += centrocampista[2]

            else:
                if difensore[2] < attaccante[2]:
                    best_formation[3].append(attaccante[0])
                    index_att += 1
                    counter_role['A'] += 1
                    total += attaccante[2]
                else:
                    best_formation[1].append(difensore[0])
                    index_dd += 1
                    counter_role['D'] += 1
                    total += difensore[2]

    for sublist in best_formation:
        for player in sublist:
            print(player)

    fill_best_formation(ws, best_formation, team_name)

wb = load_workbook('/Users/marcomelis/Dropbox/Mia/File excel/Fantacalcio/2019-2020/Fantacalcio 2019-2020 best.xlsx')



portieri = []
difensori = []
centrocampisti = []
attaccanti = []

for giornata in range(1, 29):
    print(f'Giornata numero {giornata}')
    formations = load(open(f'resource/Formazioni/Giornata{giornata}.json'))
    votes = load(open(f'resource/Voti ufficiosi/Json/Giornata {giornata+2}.json'))
    ws = wb[f'Giornata {giornata}']
    for team_name in ['Melis', 'Milo', 'Sangio', 'Giulio', 'Zone', 'Carlo', 'Bisca', 'Pietro', 'Zino', 'Michelone']:
        for number in range(1, 12):
            player = formations[f'Giornata{giornata}'][team_name]['titolari'][str(number)].upper()
            try:
                role = votes[player]['Ruolo']
                if role == 'P' and votes[player]['G'] == 's.v':
                    vote = 7
                elif role == 'P' and votes[player]['GS'] == 0:
                    vote = votes[player]['G'] + votes[player]['GF']*3 + 1 - votes[player]['Aut']*3 \
                            + votes[player]['Ass'] - votes[player]['Amm']*0.5 - votes[player]['Esp'] - votes[player]['RigS']*3 \
                            + votes[player]['RigP']*3

                else:
                    vote = votes[player]['G'] + votes[player]['GF'] * 3 - votes[player]['GS'] - votes[player]['Aut'] * 3 + votes[player]['Ass'] - votes[player]['Amm'] * 0.5 - votes[player]['Esp'] - votes[player]['RigS'] * 3 + votes[player]['RigP']*3
                if role == 'P':
                    portieri.append([player, role, vote])
                elif role == 'D':
                    difensori.append([player, role, vote])
                elif role == 'C':
                    centrocampisti.append([player, role, vote])
                elif role == 'A':
                    attaccanti.append([player, role, vote])
            except KeyError:
                pass
            except TypeError:
                pass

        len_riserve = len(formations[f'Giornata{giornata}'][team_name]['riserve'])
        for number in range(1, len_riserve):
            player = formations[f'Giornata{giornata}'][team_name]['riserve'][str(number)].upper()
            try:
                role = votes[player]['Ruolo']
                if role == 'P' and votes[player]['GS'] == 0:
                    vote = votes[player]['G'] + votes[player]['GF'] * 3 + 1 - votes[player]['Aut'] * 3 \
                           + votes[player]['Ass'] - votes[player]['Amm'] * 0.5 - votes[player]['Esp'] - votes[player][
                               'RigS'] * 3 \
                           + votes[player]['RigP'] * 3
                    if role == 'P':
                        portieri.append([player, role, vote])
                    elif role == 'D':
                        difensori.append([player, role, vote])
                    elif role == 'C':
                        centrocampisti.append([player, role, vote])
                    elif role == 'A':
                        attaccanti.append([player, role, vote])
                else:
                    try:
                        vote = votes[player]['G'] + votes[player]['GF'] * 3 - votes[player]['GS'] - votes[player]['Aut'] * 3 + \
                               votes[player]['Ass'] - votes[player]['Amm'] * 0.5 - votes[player]['Esp'] - votes[player][
                                   'RigS'] * 3 + votes[player]['RigP'] * 3
                        if role == 'P':
                            portieri.append([player, role, vote])
                        elif role == 'D':
                            difensori.append([player, role, vote])
                        elif role == 'C':
                            centrocampisti.append([player, role, vote])
                        elif role == 'A':
                            attaccanti.append([player, role, vote])
                    except TypeError:
                        pass

            except KeyError:
                pass

        portieri.sort(key=sorting_criteria, reverse=True)
        difensori.sort(key=sorting_criteria, reverse=True)
        centrocampisti.sort(key=sorting_criteria, reverse=True)
        attaccanti.sort(key=sorting_criteria, reverse=True)

        print(portieri)
        print(difensori)
        print(centrocampisti)
        print(attaccanti)
        create_best_formation(portieri, difensori, centrocampisti, attaccanti, team_name)

        portieri.clear()
        difensori.clear()
        centrocampisti.clear()
        attaccanti.clear()

wb.save('/Users/marcomelis/Dropbox/Mia/File excel/Fantacalcio/2019-2020/Fantacalcio 2019-2020 best.xlsx')
wb.close()
