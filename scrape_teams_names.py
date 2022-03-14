import bs4, copy


def scrape_teams_names(session, soup: bs4.BeautifulSoup, data, match_day):
    # default structure of dictionary for each player
    default_struct_dict = {
        "link": "",
        "titolari": {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": ""
      },
        "riserve": {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": ""}
    }

    #find tag that has specified class
    team = soup.find_all(class_="game-result-team-name")

    # append in data dict the home team name
    data['Giornata' + str(match_day)][team[0].text.strip()] = copy.deepcopy(default_struct_dict)

    # append in data dict the away team name
    data['Giornata' + str(match_day)][team[1].text.strip()] = copy.deepcopy(default_struct_dict)

    return data