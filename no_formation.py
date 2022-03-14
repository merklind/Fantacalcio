from re import compile


def no_formation(match_day: int, home_team_name: str, away_team_name: str, data: dict, soup):
    home_team = soup.find(id='MainContent_wuc_DettagliPartita1_PanelSquadraCasa')
    away_team = soup.find(id='MainContent_wuc_DettagliPartita1_PanelSquadraTrasferta')
    home_formation = home_team.find(class_=compile('icon icon-sm fas'))
    away_formation = away_team.find(class_=compile('icon icon-sm fas'))
    home_formation_text = home_formation['data-original-title']
    away_formation_text = away_formation['data-original-title']
    if home_formation_text == 'Schierata dall\'utente':
        data["Giornata" + str(match_day)][home_team_name]['formazione schierata'] = '√'
    else:
        data["Giornata" + str(match_day)][home_team_name]['formazione schierata'] = 'X'

    if away_formation_text == 'Schierata dall\'utente':
        data["Giornata" + str(match_day)][away_team_name]['formazione schierata'] = '√'
    else:
        data["Giornata" + str(match_day)][away_team_name]['formazione schierata'] = 'X'
