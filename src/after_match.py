from scraping.parse_voti_file import parse_voti_file
from excel_utils.insert_voti import insert_voti

match_day = int(input('Inserisci la giornata: '))
parse_voti_file(match_day)
insert_voti(match_day)
