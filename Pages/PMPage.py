from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class PMPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/PM/'
