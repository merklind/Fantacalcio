import os

from COSTANTS import URL_LOGIN, HEADERS


def login(s):
    """
    
    Esegue il login su sito di fantaservice.
    Lancia un errore se lo statud code della risposta è diverso da 200
    o se il contenuto della risposta contiene informazioni su username o password errati.

    """

    username = os.environ.get('FANTA_USER')
    password = os.environ.get('FANTA_PWD')

    if username is None or password is None:
        #raise ValueError("Username o password mancanti")
        username = 'marcomelis'
        password = 'spry334;blab'


    payload = { "ctl00$MainContent$wuc_Login1$username": username,
                "ctl00$MainContent$wuc_Login1$password": password,
                "ctl00$MainContent$wuc_Login1$btnLogin": "accedi",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATEGENERATOR": "C2EE9ABB"
                }

    # send a post request to url, with a custom
    # header and custom data to perform login
    login = s.post(URL_LOGIN, headers=HEADERS, data=payload)

    # print 'Site reachable' if status code is 200
    if(login.status_code == 200):
        print("Site reachable")
    
    else:
        print(f"Site not reachable\nStatus code:{login.status_code}")
        raise ConnectionError("Sito non raggiungibile")

    
    if "Username o Password errati" in login.text:
        raise ValueError("Username o Password errati")