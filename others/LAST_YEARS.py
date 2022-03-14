import requests, bs4, re
from src.scraping.login import login

def master():
    s = requests.Session()
    login(s)
    bs = request_page(s)
    list_team = scrape_name_team(bs)
    scrape_page(bs, list_team)

def request_page(session):
    url = "https://www.fanta.soccer/it/lega/privata/25534/riepilogolega/campionato-massena/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    req = session.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(req, 'html.parser')
    return soup

def scrape_page(Soup, list_team):
    Esito = []
    Punti = 0
    
    #Trova tutte le tabelle delle singole giornate
    Day = Soup.find_all("div", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_PanelGiornata\d_\d"))
    for team in list_team:
        for Single_Day in Day:
            Row = Single_Day.find_all("span", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_rptGiornata\d_\d*_lblPartita_\d*"))
            for Single_Row in Row:
                if team in Single_Row.text:
                    if Single_Row.text.startswith(team):
                        Goal_Miei = Single_Row.parent.parent.find("span", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_rptGiornata\d_\d*_lblGolCasa_\d*")).text
                        Goal_Avversario = Single_Row.parent.parent.find("span", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_rptGiornata\d_\d*_lblGolTrasferta_\d*")).text

                    elif Single_Row.text.endswith(team):
                        Goal_Miei = Single_Row.parent.parent.find("span", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_rptGiornata\d_\d*_lblGolTrasferta_\d*")).text
                        Goal_Avversario = Single_Row.parent.parent.find("span", id=re.compile(r"MainContent_wuc_RiepilogoLega1_wuc_Calendario1_rptCalendario_rptGiornata\d_\d*_lblGolCasa_\d*")).text
                    if int(Goal_Miei) > int(Goal_Avversario):
                        Punti += 3
                        Esito.append(Punti)
                    elif int(Goal_Miei) < int(Goal_Avversario):
                        Punti += 0
                        Esito.append(Punti)
                    elif int(Goal_Miei) == int(Goal_Avversario):
                        Punti += 1
                        Esito.append(Punti)
        print(team)                    
        print(Esito)
        Esito = []
        Punti = 0

def scrape_name_team(bs):
    list_team = []
    table_name = bs.find(id='classifica-lega').tbody
    row = table_name.find_all('tr')

    for team in row:
        name_team = team.find_all('td')[1].a.text
        list_team.append(name_team)

    return list_team



master()