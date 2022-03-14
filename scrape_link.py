import bs4

from COSTANTS import ID_LEGA


def scrape_link(session, match_day):
    links = []

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    url_calendar = f'https://www.fanta.soccer/it/lega/privata/{ID_LEGA}/calendario/{match_day}/'

    # send a post request to url_calendar with custom headers and custom payload
    req = session.post(url_calendar, headers=header)

    # retrieve text from request object
    req_text = req.text
    # create a bs4 object
    soup = bs4.BeautifulSoup(req_text, 'html.parser')


    # for each match in a specific day scrape the link
    for times in range(5):
        # extract the link from <a> tag with specific id
        link_match = soup.find('a', {'id': f'MainContent_wuc_Calendario1_rptGiornata_hlPartita_{times}'})['href']
        # append to links list the match link
        links.append(f'https://www.fanta.soccer{link_match}')

    # return the list with all the links for a specific day
    return links
