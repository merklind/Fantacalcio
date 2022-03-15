import json
from COSTANTS import CURRENT_YEAR


def change_player_name(match_day):
    input_file = open(f'resource/{CURRENT_YEAR}/Formazioni/Giornata' + match_day + '.json', 'r+')
    change_file = open(f'resource/change_name/change_name_{CURRENT_YEAR}.json', 'r')
    data = json.load(input_file)
    data_change = json.load(change_file)
    input_file.close()
    first_key = list(data.keys())[0]
    player_key = list(data[first_key])
    for single_player in player_key:
        counter = 1
        players_name = data[first_key][single_player]['titolari'].values()
        for player_name in players_name:
            if player_name in data_change:
                data[first_key][single_player]['titolari'][str(counter)] = data_change[player_name]
            counter += 1

    for single_player in player_key:
        counter = 1
        players_name = data[first_key][single_player]['riserve'].values()
        for player_name in players_name:
            if player_name in data_change:
                data[first_key][single_player]['riserve'][str(counter)] = data_change[player_name]
            counter += 1

    with open(f'resource/{CURRENT_YEAR}/Formazioni/Giornata' + match_day + '.json', 'w') as input_file:
        json.dump(data, input_file, indent=4, ensure_ascii=False)
