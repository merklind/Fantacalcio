from COSTANTS import TEAM_NAME

def change_team_name(data: dict, match_day):
    new_dict = {f'Giornata{match_day}': {}}
    # list with default change from fantacalcio names to our surname
    

    # loop through fake name and our surname to perform the change
    for team_name in data['Giornata' + match_day].keys():
        new_dict['Giornata'+ match_day][TEAM_NAME[team_name]] = data['Giornata' + match_day][team_name]

    return new_dict
