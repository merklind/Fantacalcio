import json
from json import dump
from re import compile


from src.COSTANTS import CHANGE_NAME_FILE, CURRENT_YEAR
from src.utils.change_team_name import change_team_name
from src.scraping.no_formation import no_formation
from src.scraping.scrape_teams_names import *


def scrape_player(session, match_links, match_day):

    change_name_file = open(f'resource/change_name/{CHANGE_NAME_FILE}')
    change_name_dict = json.load(change_name_file)

    soup_list = []

    # create dict object
    data = dict()

    # initialize data dict with first key
    data['Giornata' + match_day] = dict()

    for link, counter in zip(match_links, range(1, 6)):
        # send a get request to match link
        req = session.get(link)

        # retrieve text from req request
        req_text = req.text

        # create soup object
        soup = bs4.BeautifulSoup(req_text, 'html.parser')

        # append soup object to a list
        soup_list.append(soup)

        # control print
        print(str(counter) + '. link fetch')


    # loop in links list
    for soup in soup_list:

        # variable used as key in 'titolari' and 'riserve' into the data dict
        num = 1

        # insert in data dict teams name
        data = scrape_teams_names(session, soup, data, match_day)

        # retrieve the home team name
        home_team_name = soup.find('div', class_='game-info-team game-info-team-first').find('a', class_='fantasquadra').text.strip()
        # retrieve text home regular team's players
        home_regulars_players = soup.find_all('span', id=compile('MainContent_wuc_DettagliPartita1_rptTitolariCasa_lblNome_(\d)*'))
        # retrieve text home bleachers team's players
        home_bleachers_players = soup.find_all('span', id=compile('MainContent_wuc_DettagliPartita1_rptPanchinariCasa_lblNome_(\d)*'))

        # retrieve the away team name
        away_team_name = soup.find('div', class_='game-info-team game-info-team-second').find('div', class_='game-result-team-name').text.strip()
        # retrieve text away regular team's players
        away_regulars_players = soup.find_all('span', id=compile('MainContent_wuc_DettagliPartita1_rptTitolariTrasferta_lblNome_(\d)*'))
        # retrieve text away bleachers team's players
        away_bleachers_players = soup.find_all('span', id=compile('MainContent_wuc_DettagliPartita1_rptPanchinariTrasferta_lblNome_(\d)*'))

        # retrieve information about formation
        no_formation(match_day, home_team_name, away_team_name, data, soup)

        # add in data dictionary name of home regulars players
        for name_player in home_regulars_players:
            code_player = str(name_player.a['href']).split('/')[3]
            if len(code_player) == 5:
                data["Giornata" + str(match_day)][home_team_name]['titolari'][str(num)] = \
                change_name_dict[str(10) + code_player]['nome_PianetaFanta']
            elif len(code_player) == 6:
                data["Giornata" + str(match_day)][home_team_name]['titolari'][str(num)] = \
                change_name_dict[str(1) + code_player]['nome_PianetaFanta']
            num += 1

        # reset of num variable
        num = 1

        # add in data dictionary name of home bleachers players
        for name_player in home_bleachers_players:
            code_player = str(name_player.a['href']).split('/')[3]
            if len(code_player) == 5:
                data["Giornata" + str(match_day)][home_team_name]['riserve'][str(num)] = change_name_dict[str(10) + code_player]['nome_PianetaFanta']
            elif len(code_player) == 6:
                data["Giornata" + str(match_day)][home_team_name]['riserve'][str(num)] = \
                change_name_dict[str(1) + code_player]['nome_PianetaFanta']
            num += 1

        # reset of num variable
        num = 1

        # add in data dictionary name of away regulars players
        for name_player in away_regulars_players:
            code_player = str(name_player.a['href']).split('/')[3]
            if len(code_player) == 5:
                data["Giornata" + str(match_day)][away_team_name]['titolari'][str(num)] = \
                change_name_dict[str(10) + code_player]['nome_PianetaFanta']
            elif len(code_player) == 6:
                data["Giornata" + str(match_day)][away_team_name]['titolari'][str(num)] = \
                change_name_dict[str(1) + code_player]['nome_PianetaFanta']
            num += 1

        # reset of num variable
        num = 1

        # add in data dictionary name of away bleachers players
        for name_player in away_bleachers_players:
            code_player =  str(name_player.a['href']).split('/')[3]
            if len(code_player) == 5:
                data["Giornata" + str(match_day)][away_team_name]['riserve'][str(num)] = change_name_dict[str(10) + code_player]['nome_PianetaFanta']
            elif len(code_player) == 6:
                data["Giornata" + str(match_day)][away_team_name]['riserve'][str(num)] = change_name_dict[str(1) + code_player]['nome_PianetaFanta']
            num += 1

    # change the names of the teams from fantacalcio names to our surname
    data = change_team_name(data, match_day)

    member_team = list(data['Giornata' + match_day].keys())
    for num in range(0, 10, 2):
        data['Giornata' + match_day][member_team[num]]['link'] = match_links[num//2]
        data['Giornata' + match_day][member_team[num + 1]]['link'] = match_links[num//2]

    # save the dict in a json file
    with open(f'resource/{CURRENT_YEAR}/Formazioni/Giornata' + str(match_day) + '.json', 'w') as output_file:
        dump(data, output_file, indent=4, ensure_ascii=False)
