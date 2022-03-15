import requests
import bs4
from json import dump
from tqdm import tqdm
from COSTANTS import CURRENT_YEAR, URL_PIANETAFANTA_PREFIX, PROJECT_FOLDER

def parse_voti_file(match_day):

    data = dict()
    req = requests.get(URL_PIANETAFANTA_PREFIX + str(match_day + 2)  + '&searchBonus=')
    voti_file = open(f'{PROJECT_FOLDER}/rsc/{CURRENT_YEAR}/Voti ufficiosi/Html/Giornata' + str(match_day + 2) + '.html', 'w')
    voti_file.write(req.text)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    table_row = soup.find_all('tr')
    print('Parsing file voti:\n')
    for row in tqdm(table_row[4:]):
        if row.find_all('td')[0].text != 'ALL.':
            giocatore = row.find_all('td')[1].text.strip()
            data[giocatore] = dict()
            data[giocatore]['Ruolo'] = row.find_all('td')[2].text.strip()
            data[giocatore]['Squadra'] = row.find_all('td')[4].text.strip()
            if row.find_all('td')[6].text.strip() == '0':
                data[giocatore]['G'] = "s,v"
            elif row.find_all('td')[6].text.strip() != 's,v,':
                data[giocatore]['G'] = float(row.find_all('td')[6].text.replace(',', '.').strip()[:-1])
            else:
                data[giocatore]['G'] = row.find_all('td')[6].text.replace(',', '.').strip()[:-1]
            data[giocatore]['GF'] = int(row.find_all('td')[7].text.strip())
            data[giocatore]['GS'] = int(row.find_all('td')[8].text.strip())
            data[giocatore]['Aut'] = int(row.find_all('td')[9].text.strip())
            data[giocatore]['Ass'] = int(row.find_all('td')[10].text.strip())
            data[giocatore]['Amm'] = int(row.find_all('td')[23].text.strip())
            data[giocatore]['Esp'] = int(row.find_all('td')[24].text.strip())
            data[giocatore]['RigS'] = int(row.find_all('td')[27].text.strip())
            data[giocatore]['RigP'] = int(row.find_all('td')[28].text.strip())


    with open(f'{PROJECT_FOLDER}/rsc/{CURRENT_YEAR}/Voti ufficiosi/Json/Giornata ' + str(match_day + 2) + '.json', 'w') as output_file:
        dump(data, output_file, indent=4)
