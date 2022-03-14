#! /usr/bin/bash python
import requests, bs4,re, openpyxl, os


partite = []
url_login = 'http://www.fanta.soccer/it/login/'
url_calendar = 'https://www.fanta.soccer/it/lega/privata/122355/calendario/'
payload =  {"ctl00$MainContent$wuc_Login1$username": os.environ.get('FANTA_USER'),
            "ctl00$MainContent$wuc_Login1$password": os.environ.get('FANTA_PWD'),
            "ctl00$MainContent$wuc_Login1$btnLogin": "accedi",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "/wEPDwUKLTIxMjI4MjY3NA9kFgJmD2QWBAIBD2QWBgIXDxYCHgRocmVmBR8vY3NzL3N0eWxlLmNzcz9tPTIwMTgwNjE0MDgwMjM0ZAIcDxYCHgdWaXNpYmxlaGQCHQ8WAh8BaGQCAw9kFgwCAg8PFgIfAWhkZAIDDw8WAh4LTmF2aWdhdGVVcmwFAS9kZAIEDw8WAh8CBQEvZGQCBg8WAh8BaGQCCQ8WAh4LXyFJdGVtQ291bnQCAxYGZg9kFgJmDxUFEzI2LzA2LzIwMTggMTU6Mzg6MzYCMTAGMTM3NzEyMVJpcHJpc3Rpbm8gY2FsY2lhdG9yZSBuZWxsbyBzY2hpZXJhbWVudG8gdGl0b2xhcmULZGVhbmFtYnJvc2VkAgEPZBYCZg8VBRMyNC8wNi8yMDE4IDAwOjE0OjU3AjEwBjEzNzY3NGNzZWduYWxhemlvbmUgcGVyIGxvIHN0YWZmIGRpIGdyYXZlIGJ1ZyBuZWwgc2lzdGVtYSBkZWxsZSBsZWdoZSBtb25kaWFsaSwgY2hhbXBpb25zIGVkIGV1cm9wYSBsZWFndWUNZm9sbGV0dG9wYXp6b2QCAg9kFgJmDxUFEzI1LzA2LzIwMTggMTc6NDU6NDICMTAGMTM3Njk5E0NhbWJpbyBib251cyBBc3Npc3QKU2FuZHJpbm85MWQCCg8WAh4EVGV4dAU7IDxzcGFuIGNsYXNzPSJ0ZXh0LXNtYWxsIHRleHQtZGFyayI+IC0gOTQuMjMuMTgzLjEyMTwvc3Bhbj5kGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBS5jdGwwMCRNYWluQ29udGVudCR3dWNfTG9naW4xJGNoa1Jlc3RhQ29sbGVnYXRvdkEYQywo9nZROnb6hQ5ta11HG3s=",
            "__VIEWSTATEGENERATOR": "C2EE9ABB"
            }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

with requests.Session() as session:

    login = session.post(url_login, data = payload, headers = headers)
    home_page = session.get(url_calendar, headers=headers).text
    soup = bs4.BeautifulSoup(home_page, 'html.parser')
    all_match = soup.find_all(id=re.compile(r'MainContent_wuc_Calendario1_rptPartite_PanelPartita_\d'))
    for match in all_match:
        if match.find(class_='squadra_casa').a.text == ('Maori\'s club') or match.find(class_='squadra_fuoricasa').a.text == ('Maori\'s club'):
            partite.append(match.find(class_='squadra_casa').a.text)
            partite.append(match.find(class_='squadra_fuoricasa').a.text)

    
wb = openpyxl.load_workbook('/Users/marcomelis/Dropbox/Mia/File excel/Fantacalcio/2020-2021/Fantacalcio 2020-2021.xlsx')
ws = wb['Mio calendario2']
Len = len(partite)
i = 2
for Team in range(Len):
    if Team % 2 == 0:
        ws['A' + str(i)] = partite[Team]
    else:
        ws['F' + str(i)] = partite[Team]
        i += 1
wb.save('/Users/marcomelis/Dropbox/Mia/File excel/Fantacalcio/2020-2021/Fantacalcio 2020-2021.xlsx')
wb.close()
print('Ok!')




