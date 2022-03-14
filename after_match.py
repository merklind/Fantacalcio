#!/usr/local/Cellar/python/3.7.2_2/bin/python3.7

from parse_voti_file import parse_voti_file
from insert_voti import insert_voti

match_day = int(input('Inserisci la giornata: '))
parse_voti_file(match_day)
insert_voti(match_day)
