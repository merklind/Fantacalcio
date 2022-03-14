from tkinter import *
from login import login
from requests.sessions import Session
from scrape_link import scrape_link
from scrape_player import scrape_player
from fill_info_excel import fill_info_excel
import threading

class MainWindow():

    def __init__(self, window):

        self.window = window
        self.window.title('Fantacalcio')

        self.lbl_giornata = Label(master=self.window, text='Inserisci la giornata:')
        self.etr_giornata = Entry(master=self.window)
        self.btn_ok = Button(master=self.window, text='Run', command=self.start_activity)


        self.lbl_giornata.pack()
        self.etr_giornata.pack()
        self.btn_ok.pack()

    def start_activity(self):

        t = threading.Thread()
        t.__init__()
        t.start()


        def run():
            s = Session()
            login(s)
            num_giornata = self.etr_giornata.get()
            match_links = scrape_link(s, num_giornata)
            scrape_player(s, match_links, num_giornata)
            fill_info_excel(num_giornata)



root = Tk()
MainWindow(root)
root.mainloop()