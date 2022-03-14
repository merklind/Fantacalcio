import requests
import bs4
from login import login
from time import sleep

def retrieve_calendar():

    home = []
    away = []
    data = {
        'Mastini na...':'Milo',
        'Gramentela':'Gracis',
        'Patchester...':'Sangio',
        'SPORTING Z...':'Michelone',
        'SSC Otto':'Pietro',
        'Spartak Bisca':'Bisca',
        'Maori\'s club':'Melis',
        'G.S. Ambro...':'Zino',
        'FC POLO SPORT':'Zone',
        'f.c. panda':'Carlo'
    }

    s = requests.Session()

    login(s)


    for match_day in range(1, 37):
        print(str(match_day))
        url_calendar = 'https://www.fanta.soccer/it/lega/privata/122355/calendario/' + str(match_day) + '/'
        #sleep(5)
        req = s.get(url_calendar)
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        home_divs = soup.find_all('div', class_='game-result-team game-result-team-horizontal game-result-team-first')
        away_divs = soup.find_all('div', class_='game-result-team game-result-team-horizontal game-result-team-second')
        for home_div in home_divs:
            home.append(home_div.find('div', class_='game-result-team-title').text.strip())
        for away_div in away_divs:
            away.append(away_div.find('div', class_='game-result-team-title').text.strip())

    for index in range(len(home)):
        home[index] = data[home[index]]

    for index in range(len(away)):
        away[index] = data[away[index]]

    print(home)
    print(away)

retrieve_calendar()

