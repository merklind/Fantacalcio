import bs4

from COSTANTS import HEADERS, URL_CALENDAR


def scrape_link(session, match_day):
    links = []

    url_calendar = f'{URL_CALENDAR}/{match_day}/'

    # send a post request to url_calendar with custom headers
    req = session.post(url_calendar, headers=HEADERS)

    # retrieve text from request object
    req_text = req.text
    # create a bs4 object
    soup = bs4.BeautifulSoup(req_text, 'html.parser')


    # for each match in a specific day scrape the link
    for idx_match in range(5):
        # extract the link from <a> tag with specific id
        link_match = soup.find('a', {'id': f'MainContent_wuc_Calendario1_rptGiornata_hlPartita_{idx_match}'})['href']
        # append to links list the match link
        links.append(f'https://www.fanta.soccer{link_match}')

    # return the list with all the links for a specific day
    return links
