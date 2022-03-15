from pathlib import Path

#Costanti utili per lo scraping
URL_LOGIN = f'http://www.fanta.soccer/it/login/'
URL_PIANETAFANTA_PREFIX = 'https://www.pianetafanta.it/Voti-Ufficiosi-Excel.asp?giornataScelta='

HEADERS = {
	
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}

ID_LEGA_VECCHIO = f'122355'
ID_LEGA = f'134373'
URL_CALENDAR = f'https://www.fanta.soccer/it/lega/privata/{ID_LEGA}/calendario'
CHANGE_NAME_FILE = f'change_name_2021-2022.json'
CURRENT_YEAR = f'2021-2022'
FILE_PATH = r'C:\Users\mmelis\Downloads\2021-2022\2021-2022\Fantacalcio 2021-2022.xlsx'
FILE_ASS_FANTASERVICE_PIANETAFANTA_PATH = r"C:\Users\mmelis\Downloads\2021-2022\2021-2022\Associazione giocatori FantaService-PianetaFanta.xlsx"
PROJECT_FOLDER = Path(__file__).parent.parent

TEAM_NAME = {
	"Fc Nando Kill-bisk": "Bisca",
	"SSC Otto": "Pietro",
	"ZEON CAVALLO": "Zone",
	"G.S. Ambrosiana": "Zino",
	"Mastini napoleta...": "Milo",
	"AZTECHI MILANO": "Michelone",
	"Patchester United": "Sangio",
	"Maori's club": "Melis",
	"Gramentela": "Gracis",
	"f.c. panda": "Carlo"
}
