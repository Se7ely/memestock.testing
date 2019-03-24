from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class UserSettingsPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/Settings/'
        self.accounttab='//a[@href="/Settings/Account"]'
        self.profiletab='//a[@href="/Settings/Profile"]'

