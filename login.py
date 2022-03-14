import os

from COSTANTS import URL_LOGIN


def login(s):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    payload = { "ctl00$MainContent$wuc_Login1$username": os.environ.get('FANTA_USER'),
                "ctl00$MainContent$wuc_Login1$password": os.environ.get('FANTA_PWD'),
                "ctl00$MainContent$wuc_Login1$btnLogin": "accedi",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATEGENERATOR": "C2EE9ABB"
                }

    # send a post request to url, with a custom
    # header and custom data to perform login
    login = s.post(URL_LOGIN, headers=header, data=payload)

    # print 'Site reachable' if status code is 200
    if(login.status_code == 200):
        print("Site reachable")
