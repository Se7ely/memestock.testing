from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class SettingsPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/Settings/'
        self.accounttab='//a[@href="/Settings/Account"]'
        self.profiletab='//a[@href="/Settings/Profile"]'


    def GetAccountTab(self, driver):
        return driver.find_element_by_xpath(self.accounttab)

    def GetProfileTab(self, driver):

        return driver.find_element_by_xpath(self.profiletab)



