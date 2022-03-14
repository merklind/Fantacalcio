from requests import Session
import pprint

headers = {
    'authority': 'www.fanta.soccer',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'x-microsoftajax': 'Delta=true',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.fanta.soccer',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.fanta.soccer/it/login/',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.1.25914076.1585746344; googlepersonalization=OxLbC_OxLbC_gA; eupubconsent=BOxLbC_OxLbC_AKAAAENAAAA-AAAAA; euconsent=BOxLbC_OxLbC_AKAABENDD-AAAAutr_7__7-_9_-_f__9uj3Gr_v_f__32ccL59v_h_7v-_7fi_-0nV4u_1vft9yfk1-5ctDztp507iakiPHmqNeb9n_mz1e5pRP78k09r5337Ew_v8_v-b7BCPN9Y3v-w; _pubCommonId=6dc8623a-1d12-4d23-9705-92f860557b97; _pubCommonId_last=Wed%2C%2001%20Apr%202020%2013%3A05%3A49%20GMT; __gads=ID=36d19d554b6d8330:T=1585746349:S=ALNI_MYB60lwRe5ZZr-GgxATXUvT7nHqBQ; __atuvc=31%7C14; cto_bidid=XkPTW19Gck9aYUIwMTExNUkxcFVONEZ4eE1oOFhYZzAyJTJGUktHRmJ2dTJCWmFSTzJWM3VZVTRSdWxLU1BGclZwR2YwRkJyWDFtcVFWZCUyRlBkNXlOdHRwJTJCVXhoUW9RSzI5SUV6bWRYWEVVV0FxeTlrOCUzRA; cto_bundle=mGuGJl9tNEZjaUlhWHBXcXVhaHRFa1dSR2QlMkJCUkJhcEV6SkJPZEFsU2U3R0JITG9KV3RJaUVRWXdVZyUyRm1JN3EwWVkzYjZhMnphVURuYW1wVUNOWkVzbFF6T2M5SlBPOSUyQjFQbDU0QXJ3TXpreEZ6bERSN2FiTUx6b1dKOFB4VHFKZ1lPRUdIRWw4NE5sRVhHZ0tVRWxBZW5idVElM0QlM0Q; _ga_FRMCW717B4=GS1.1.1585773026.6.0.1585773026.0; ASP.NET_SessionId=341easpwrcdrd33ap2k5rpnh',
}

data = {
  'ctl00$smFantaSoccer': 'ctl00$MainContent$wuc_Login1$upLogin|ctl00$MainContent$wuc_Login1$btnLogin',
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwUKMTY3MTAyNDQ3Nw9kFgJmD2QWBAIBD2QWBAITDxYCHgRocmVmBR8vY3NzL3N0eWxlLmNzcz9tPTIwMjAwOTEyMDEyODEzZAIZDxYCHgRUZXh0BUI8bGluayByZWw9ImNhbm9uaWNhbCIgaHJlZj0iaHR0cHM6Ly93d3cuZmFudGEuc29jY2VyL2l0L2xvZ2luLyIgLz5kAgMPFgIeBmFjdGlvbgUKL2l0L2xvZ2luLxYQAgIPFgIfAQUFZmFsc2VkAgUPDxYCHgtOYXZpZ2F0ZVVybAUKL2l0L2xvZ2luL2RkAgYPDxYCHgdWaXNpYmxlaGRkAggPFgIfBGhkAgkPZBYQAgEPFgIfAQUTTGlndWUgMSAtIDIwMjAvMjAyMWQCAw8WAh8BBSRkb21lbmljYSAxMyBzZXR0ZW1icmUgMjAyMCBvcmUgMTM6MDBkAgUPDxYEHghJbWFnZVVybAUYL0ltYWdlcy9zY3VkZXR0aS84OTUucG5nHg1BbHRlcm5hdGVUZXh0BQVGYWxzZWRkAgcPFgIfAQUFTGlsbGVkAgkPDxYEHwUFGC9JbWFnZXMvc2N1ZGV0dGkvODk2LnBuZx8GBQVGYWxzZWRkAgsPFgIfAQUHRkMgTWV0emQCDQ8WAh8BBYUBPGRpdiBjbGFzcz0iY291bnRkb3duIGNvdW50ZG93bi1jbGFzc2ljIiBkYXRhLXR5cGU9InVudGlsIiBkYXRhLXRpbWU9IjEzIFNlcCAyMDIwIDEzOjAwIiBkYXRhLWZvcm1hdD0iZGhtcyIgZGF0YS1zdHlsZT0ic2hvcnQiPjwvZGl2PmQCDw8PFgIfAwUnL2l0L3NlcmllYS82MDg2OC9wYXJ0aXRhL2xpbGxlLWZjX21ldHovZGQCDA9kFgZmDxYCHwEFE0FjY2VkaSAvIFJlZ2lzdHJhdGlkAgIPDxYEHwEFB0FjY291bnQfAwUBI2RkAgMPFgIfAQUVQWNjZWRpIGEgRmFudGEuU29jY2VyZAIOD2QWAgIBD2QWAgILD2QWAmYPZBYGAg0PFgIfAQVTQWNjb25zZW50byBhbCB0cmF0dGFtZW50byBkZWkgbWllaSBkYXRpIHBlcnNvbmFsaSBjb21lIGRhIEluZm9ybWF0aXZhIHN1bGxhIFByaXZhY3lkAg8PFgIfAQVbQWNjb25zZW50byBhbGxhIHJpY2V6aW9uZSBkaSBlbWFpbCBxdWFsaSBub3RpZmljaGUgZS9vIGNvbnRlbnV0aSBkZWxsYSBwaWF0dGFmb3JtYSBkaSBnaW9jb2QCEQ8WAh8BBT1BY2NvbnNlbnRvIGFsbGEgcmljZXppb25lIGRpIGVtYWlsIGNvbiBjb250ZW51dG8gcHJvbW96aW9uYWxlZAIPDxYCHwEFNyA8c3BhbiBjbGFzcz0idGV4dC1zbWFsbCB0ZXh0LWRhcmsiPiAtIDEwLjAuMC41Mzwvc3Bhbj5kGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYEBS5jdGwwMCRNYWluQ29udGVudCR3dWNfTG9naW4xJGNoa1Jlc3RhQ29sbGVnYXRvBSdjdGwwMCRNYWluQ29udGVudCR3dWNfTG9naW4xJGNoa1ByaXZhY3kFKmN0bDAwJE1haW5Db250ZW50JHd1Y19Mb2dpbjEkY2hrTmV3c2xldHRlcgUjY3RsMDAkTWFpbkNvbnRlbnQkd3VjX0xvZ2luMSRjaGtERU18/7N5O2i0pZ3+AkGZADnkibv9yA==',
  '__VIEWSTATEGENERATOR': 'C2EE9ABB',
  'ctl00$MainContent$wuc_Login1$username': 'marcomelis',
  'ctl00$MainContent$wuc_Login1$password': 'spry334;blab',
  'ctl00$MainContent$wuc_Login1$cmbSesso': 'M',
  'ctl00$MainContent$wuc_Login1$txtNome': '',
  'ctl00$MainContent$wuc_Login1$txtCognome': '',
  'ctl00$MainContent$wuc_Login1$txtEmail': '',
  'ctl00$MainContent$wuc_Login1$txtConfermaEmail': '',
  'ctl00$MainContent$wuc_Login1$txtUsername': '',
  'ctl00$MainContent$wuc_Login1$txtPassword': '',
  'ctl00$MainContent$wuc_Login1$txtConfermaPassword': '',
  '__ASYNCPOST': 'true',
  'ctl00$MainContent$wuc_Login1$btnLogin': 'accedi'
}

s = Session()
response = s.post('https://www.fanta.soccer/it/login/', headers=headers, data=data)

home_page = s.get('https://www.fanta.soccer/it/lega/privata/122355/homelega/fantamassena-2020-2021/', headers=headers)
pprint.pprint(home_page.content)

