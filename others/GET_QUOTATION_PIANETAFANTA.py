from requests import get

url = f'https://www.pianetafanta.it/Giocatori-Quotazioni-Excel.asp?giornata=0&Nome=&Squadre=&Ruolo=&Ruolo2=&Quota=&Quota1=&Testata=0'
req = get(url)
quotazioni = open(f'/Users/marcomelis/Desktop/Quotazioni.xlsx', 'w')
quotazioni.write(req.text)