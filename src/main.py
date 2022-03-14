#!/usr/local/bin/python3.8

import threading

import requests

from src.excel_utils.fill_info_excel import *
from src.input_utils.input_day import *
from src.scraping.login import *
from src.scraping.scrape_link import *
from src.scraping.scrape_player import *
from utils.utility import open_wb

#Open workbook in a separate thread
wb = []
t1 = threading.Thread(target=open_wb, args=(wb, ))
t1.start()


# Create a session
s = requests.Session()

# Perform login to the site
login(s)

# Ask the user to input the number of the da
match_day = input_day()

# Scrape all match link of specific day
match_links = scrape_link(s, match_day)

# Scrape teams names, home/away regulars players, home/away bleachers players
scrape_player(s, match_links, match_day)

#wait thread t1 finished
t1.join()

# Fill excel worksheets with regular player name, bleacher player name,
# name of the team and hyperlink to each match
fill_info_excel(wb[0], match_day)